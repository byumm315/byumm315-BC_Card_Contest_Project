#필요한 패키지
import numpy as np
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
#naver map api key
client_id = 'tz5pjjcme4';    # 본인이 할당받은 ID 입력
client_pw = 'N4psultFnvcO56igYD3GLPnpVIxf8HdUHjfTfRTn';    # 본인이 할당받은 Secret 입력

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

#데이터 불러오기
from google.colab import drive
drive.mount('/content/drive') 
import pandas as pd
data=pd.read_csv('/content/drive/MyDrive/Geocoding_Input_공모전.csv') 

# 네이버 지도 API 이용해서 위경도 찾기
geo_coordi = []     
for add in data['address']:
    add_urlenc = parse.quote(add)  
    url = api_url + add_urlenc
    request = Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_pw)
    try:
        response = urlopen(request)
    except HTTPError as e:
        print('HTTP Error!')
        latitude = None
        longitude = None
    else:
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)   # json
            if response_body['addresses'] == [] :
                print("'result' not exist!")
                latitude = None
                longitude = None
            else:
                latitude = response_body['addresses'][0]['y']
                longitude = response_body['addresses'][0]['x']
                print("Success!")
        else:
            print('Response error code : %d' % rescode)
            latitude = None
            longitude = None

    geo_coordi.append([latitude, longitude])

np_geo_coordi = np.array(geo_coordi)

#데이터프레임만들기
pd_geo_coordi = pd.DataFrame({"음식점": data['restaurant'].values,
                              "도로명": data['address'].values,
                              "위도": np_geo_coordi[:, 0],
                              "경도": np_geo_coordi[:, 1]})

#데이터 저장하기
pd_geo_coordi.to_csv('info_new.csv',encoding='utf-8-sig',index=False)
