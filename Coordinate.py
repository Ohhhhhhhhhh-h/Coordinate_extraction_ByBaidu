import requests
import json
import ByBaiduapi


area_name = "阳坊镇"
guide_search_url = "https://restapi.amap.com/v3/place/text?"
form_date = {
    "key": "f725388b84d38527a644f0f234f23045",
    "keywords": area_name,
    "city": 110000,
    "citylimit": "true",
}
resp = json.loads(requests.get(url=guide_search_url, params=form_date).text)['pois'][0]['id']
# print(resp)
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71",
    "cookie": "_uab_collina=164959292696759410447469; xlly_s=1; cna=zyspGNsIN2ICAXWXPf/NAEed; gray_auth=2; oauth_state=cb5d3ff2b73bf8fd8dde8231af5f07f6; passport_login=NDUxMDMzODgzLGFtYXBfMTc3ODk2NzUzMDhCR0d4cDVLSzMsNWF3YzN6dXNsb3Z0M3k0ZXlzNGE3enczcGJmemNlc2csMTY1ODkxMDExNCxaVEJrTURnMlpHUTNNRGhrTW1RNVlUZ3hOVEZsTldOaE5ETXlPRGN5WTJNPQ==; dev_help=snR2MrhtuzMLE+9Cl8iZqmRkNDA0ODUwMTU4ZTk0NmU4MGQ3OWQ5YjNhOWQyYTk5ZjE0ZDhlZThiMmQxNTU3MDgxZmEzMjhmZWRhMWQ1ODNspIktZBKIWmSKm61YvPrHB3B4pctqFW4YCnEDxqULnPT7p0Fkpp8aOXMQ6kqCMxCXrFEYitYrSqubMTsz5YoZVK/aJRKdJQX+duB5Te5fsfEb4H/LktQsHhkjxtReY8GhalT+HM1FuxC4lmn9pJGt; x5sec=7b227761676272696467652d616c69626162612d616d61703b32223a22653439626131643162303239613131656632643239653835626331653061643443492b5a684a6347454a6939746248476f35766c6b514577366f4b563451593d227d; isg=BOLiW-k19NzENOgzlrZhF5wHM2hEM-ZNI9hgayx7gNUA_4N5FMBPX_F-KzsDb17l; l=eBS1H4QqLioRqtIdBO5ZPurza77OiIRb8sPzaNbMiInca6OCtFMXbNCHcHMeSdtjgtfXCetyac9IRdhySy4T5NkDBeYBXSaOMxJ9-; tfstk=cVUfBwaiQKvjhWXSUm1PbZQqgrgNZ-8S6iGLGTAkLoNGtfVfihTEdt53jd0Z6b1.."
}
typecode = "130400"
area_coordinate_url = f"https://ditu.amap.com/detail/get/detail?id={resp}"
print(area_coordinate_url)
resp2 = requests.get(area_coordinate_url, headers=header)
print(resp2.json())
