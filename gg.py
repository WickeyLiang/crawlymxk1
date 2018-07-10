import requests

url = "http://ku.gamersky.com/SearchGameLibAjax.aspx"

querystring = {"callback":"jQuery18302977254640576621_1529405300028","jsondata":"{rootNodeId:20039,pageIndex:1,pageSize:36,sort:'00'}","_":"1529405300244"}

headers = {
    'accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    'x-devtools-emulate-network-conditions-client-id': "CF5A04D0B49EE60333CE9BBD52B1E8AF",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36",
    'referer': "http://ku.gamersky.com/sp/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.9",
    'cookie': "UM_distinctid=160de1ef9504be-06052b0c48f554-632a7b23-1fa400-160de1ef951707; Search=1; CNZZDATA5448511=cnzz_eid%3D55662190-1521446096-http%253A%252F%252Fku.gamersky.com%252F%26ntime%3D1521446096; Hm_lvt_dcb5060fba0123ff56d253331f28db6a=1527487056,1528703803,1529391966,1529405155; Hm_lpvt_dcb5060fba0123ff56d253331f28db6a=1529405300",
    'cache-control': "no-cache",
    'postman-token': "70868e70-03d3-27c5-84c9-8d7e451d4ec1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
