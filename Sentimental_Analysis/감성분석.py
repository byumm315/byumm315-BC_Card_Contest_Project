"""##감성분석"""

##KNU 감성사전에서 팀원과 의논해 음식 도메인 사전을 구축함: 감성분석_Input_음식도메인사전
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
lexicon=pd.read_csv('/content/drive/MyDrive/감성분석_Input_음식도메인사전.csv',sep=',',encoding="cp949")

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
data_3=pd.read_csv('/content/drive/MyDrive/감성분석_Input_망고플레이트_형태소.csv',sep=',',encoding="cp949")

X=[[]]*len(data_3)
for i in range(len(data_3)):
    X[i] = data_3.iloc[i,0].split(' ')

lexicon.word.tolist()

##감성점수를 부여하는 과정
A=[0]*len(data_3)
B=[0]*len(data_3)
C=[0]*len(data_3)
for i in range(len(data_3)):
  for j in range(len(X[i])):
    if X[i][j] in lexicon.word.tolist():
      A[i]+=lexicon.polarity.tolist()[lexicon.word.tolist().index(X[i][j])]
      B[i]+=1

for i in range(len(C)):
  if B[i]!=0:
    C[i]=round(int(A[i])/int(B[i]),2)

C

data_3[['감성점수']]=C

data_3.to_csv('감성분석_Result_리뷰감성.csv',index=False)
