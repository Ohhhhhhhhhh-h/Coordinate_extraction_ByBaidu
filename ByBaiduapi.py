# 王术澔
# 时间  2022/7/27 18:40
import requests
import json
from requests.adapters import HTTPAdapter


ak = "G3pEvudnyY8cPxOhe1OOh759Ga2ibatw"
query = "南池子社区"
region = "北京"


def GetNameAndUid(query, region, ak):
    Uid_url = "http://api.map.baidu.com/place/v2/search?"

    # 请求参数
    params = {
        "query": query,
        "region": region,
        "ak": ak,
        "output": "json",
        "city_limit": "true",
        'page_num': 0,
        'total': 1
    }
    # 请求数据
    request = requests.get(Uid_url, params=params)
    # 数据的总条数
    total = json.loads(request.text)['total']
    # 每个页面大小是20，计算总页码
    total_page_num = 1  # (total + 19) // 20
    names = []
    uids = []
    for i in range(total_page_num):
        # params['page_num'] = i
        request = requests.get(Uid_url, params=params)
        for item in json.loads(request.text)['results']:
            name = item['name']
            uid = item.get('uid', '')
            names.append(name)
            uids.append(uid)
    # print(names, uids)
    return uids


# GetNameAndUid(query, region, ak)


def GetBoundary(uid):
    bmap_boundary_url = 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=ext&uid=' + uid + '&c=340&ext_ver=new&tn=B_NORMAL_MAP&nn=0&auth=fw9wVDQUyKS7%3DQ5eWeb5A21KZOG0NadNuxHNBxBBLBHtxjhNwzWWvy1uVt1GgvPUDZYOYIZuEt2gz4yYxGccZcuVtPWv3GuxNt%3DkVJ0IUvhgMZSguxzBEHLNRTVtlEeLZNz1%40Db17dDFC8zv7u%40ZPuxtfvSulnDjnCENTHEHH%40NXBvzXX3M%40J2mmiJ4Y&ie=utf-8&l=19&b=(12679382.095,2565580.38;12679884.095,2565907.38)&t=1573133634785'

    session = requests.session()
    session.mount('http://', HTTPAdapter(max_retries=3))
    session.mount('https://', HTTPAdapter(max_retries=3))
    response_2 = session.get(url=bmap_boundary_url, timeout=5, headers={"Connection": "close"})
    boundary_date = response_2.json()
    print(boundary_date)
for uid in GetNameAndUid(query, region, ak):
    GetBoundary(uid)
