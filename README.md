# byumm315-BC_Card_Contest_Project
BC카드 금융 빅데이터 플랫폼 활용 아이디어 공모전에 공모한 '리뷰기반식당추천시스템'  파이썬 코드입니다.

**진행과정**

**1. Crawling**

Crawling 폴더에 파이썬 코드와 결과 파일 있습니다.

**2. 형태소분석**

Stemming 폴더에 파이썬 코드와 결과 파일 있습니다.

**3. 연관성점수 계산**

Word2Vec_DTM 폴더에 파이썬 코드와 결과 파일 있습니다.

[세부적인 진행과정]

1. 맛집 리뷰 단어 빈도 추출
2. 단어 빈도 추출 결과, 가격, 맛, 분위기, 서비스, 웨이팅 카테고리를 선정함
3. Word2Vec과 단어-문서 행렬을 이용한 리뷰와 카테고리별 연관성 점수 계산
   1) Word2Vec을 이용해 카테고리 단어별 코사인 유사도가 높은 단어를 구할 수 있다.
   2) 카테고리 단어와 다른 단어들의 코사인 유사도 행렬을 구할 수 있다.
   3) 단어-문서 행렬(DTM Matrix) 구하기 
   4) 카테고리별 리뷰의 연관성 점수 구하기

**4. 감성분석**

Sentimental Analysis 폴더에 파이썬 코드와 결과 파일 있습니다.

**5.고객과 식당간의 거리 구하기**

Geocoding 폴더에 파이썬 코드와 결과 파일 있습니다.

**6.연관성점수와 감성점수, 가고싶다수, 평점을 반영한 고객의 식당 선호도 점수 계산은 엑셀로 했습니다.**

1.data_공모전_Weight_1121_1는 고객의 식당 선호도 점수를 계산하기 전에, 연관성점수와 감성점수, 가고싶다수, 평점을 반영해 계산한 값입니다.

2.data_공모전_Final_1121_1은 앞에서 구한 값을 식당별로 평균을 매겨, 식당별 고객의 선호도 점수를 계산한 값입니다.

3.data_공모전_Result_1121_1은 고객의 선호도 점수가 가장 높은 순서로 식당 리스트를 생성한 결과입니다.

고객이 맛을 선택했다면, 맛에서 가장 선호도 점수가 높은 식당 리스트를 추천합니다. 여기에 위치를 반영하면 반경 30Km내에 있는 식당 기준으로 추천할 수 있습니다.
