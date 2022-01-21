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

**7.결과는 Result_Files 폴더, 'data_공모전_Result_1121_1' 파일에 있습니다.**
