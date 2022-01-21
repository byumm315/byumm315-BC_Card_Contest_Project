"""##맛집 리뷰 형태소 분석"""

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
TOTAL=pd.read_csv('/content/drive/MyDrive/형태소분석_Input_망고플레이트.csv',sep=',',encoding="cp949")

import re
okt=Okt()
ii=[]
data_1=TOTAL.dropna(axis=0)
PP=[]
AA=[]
BB=[]
CC=[]
DD=[]
EE=[]
FF=[]
PP_1=[]

for i in range(len(data_1)):
  PP.append(data_1.iloc[i,0]) #review
  PP_1.append(data_1.iloc[i,0]) #raw
  AA.append(data_1.iloc[i,1]) #ID
  BB.append(data_1.iloc[i,2]) #title
  CC.append(data_1.iloc[i,3]) #taste
  DD.append(data_1.iloc[i,4]) #load
  EE.append(data_1.iloc[i,5])
  FF.append(data_1.iloc[i,6])

for i in range(len(PP)):
  PP[i]=re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]"," ", PP[i])
  PP[i]=okt.morphs(PP[i],norm=True, stem=True)
  PP[i]=[x for x in PP[i] if len(x)>1]
  PP[i]=' '.join(PP[i])

data_2=pd.DataFrame({'review':PP,'ID':AA,'title':BB,'taste':CC,'raw':PP_1,'load':DD,'가고싶다':EE,'평점':FF})

hangul = re.compile('[ㄱ-ㅣ가-힣]+')

for i in range(len(data_2)):
  if len(hangul.findall(data_2.iloc[i,0]))>1:
    if len(data_2.iloc[i,0])>1:
      ii.append(i)

data_3=data_2.iloc[ii,:]
data_3.to_csv('형태소분석_Result_망고플레이트.csv',index=False)
