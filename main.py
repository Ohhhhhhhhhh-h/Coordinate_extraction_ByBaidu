import pandas as pd
import Coordinate_processing
import shpwrite
import ByBaiduapi

query = "小区"
region = "北京"
ak = "G3pEvudnyY8cPxOhe1OOh759Ga2ibatw"
# WriteVectorFile = shpwrite.WriteVectorFile()

# 获取北京所有公园的 name 和 uid
names, uids = ByBaiduapi.GetNameAndUid(query, region, ak)

for i in range(len(names)):
    try:
        # 通过uid获取边界坐标(百度米制)
        boundarys = ByBaiduapi.GetBoundary(uids[i])
        c1 = pd.DataFrame(boundarys)
        c1.to_csv('csv', encoding='utf-8-sig')
        # 百度米制坐标转百度经纬度坐标系
        boundarys_bd09 = Coordinate_processing.bd09_metre_to_degree(boundarys, ak)
        # 百度经纬度坐标系转wgs84
        boundarys_wgs84 = Coordinate_processing.bd09_to_wgs84_batch(boundarys_bd09)
        # 写shp需要的格式
        POLYGON = "POLYGON ((" + boundarys_wgs84 + "))"
        # 写shp
        shpwrite.WriteVectorFile("shapefile//" + names[i] + ".shp", names[i], POLYGON)
    except:
        pass


