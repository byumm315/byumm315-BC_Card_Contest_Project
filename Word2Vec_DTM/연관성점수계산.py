"""##맛집 리뷰 단어 빈도 추출"""
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
A=pd.read_csv('/content/drive/MyDrive/연관성점수계산_Input_망고플레이트.csv',sep=',',encoding="cp949")

##단어 빈도 추출 결과, 카테고리: 가격, 맛, 분위기, 서비스, 웨이팅 카테고리를 생성함
A=data_3.review.to_list()
B=[]
for i in range(len(A)):
  B+=A[i].split(' ')

words_count={}
for word in B:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
sorted_words = sorted([(k,v) for k,v in words_count.items()], key=lambda word_count: -word_count[1])
print([w[0] for w in sorted_words])

"""
##Word2Vec과 단어- 행렬을 이용한 리뷰와 카테고리별 연관성 점수 계산"""

##Word2Vec 카테고리별 코사인 유사도가 높은 단어를 구할 수 있다.
X=[[]]*len(data_3)
for i in range(len(data_3)):
    X[i] = data_3.iloc[i,0].split(' ')

from gensim.models import Word2Vec
model_w = Word2Vec(sentences=X,size=500,window=5,min_count=2,workers=4,sg=1)

model_w.wv.most_similar('가격',topn=20)

df1=pd.DataFrame(model_w.wv.most_similar('맛있다',topn=20),columns=['단어','맛있다'])
df2=pd.DataFrame(model_w.wv.most_similar('가격',topn=20),columns=['단어','가격'])
df3=pd.DataFrame(model_w.wv.most_similar('웨이팅',topn=20),columns=['단어','웨이팅'])
df4=pd.DataFrame(model_w.wv.most_similar('서비스',topn=20),columns=['단어','서비스'])
df5=pd.DataFrame(model_w.wv.most_similar('분위기',topn=20),columns=['단어','분위기'])

A=list(set(df1.단어.tolist()+df2.단어.tolist()+df3.단어.tolist()+df4.단어.tolist()+df5.단어.tolist()))

A=sorted(A)

##카테고리와 단어의 코사인 유사도 행렬을 구할 수 있다.
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
A=pd.read_csv('/content/drive/MyDrive/연관성점수계산_Input_망고플레이트_1.csv',sep=',',encoding="cp949")

A=A.iloc[:,0].tolist()

A=sorted(A)

A

B_맛있다=[]
B_가격=[]
B_웨이팅=[]
B_서비스=[]
B_분위기=[]
for i in range(len(A)):
  B_맛있다.append(model_w.wv.similarity('맛있다',A[i]))
  B_가격.append(model_w.wv.similarity('가격',A[i]))
  B_웨이팅.append(model_w.wv.similarity('웨이팅',A[i]))
  B_서비스.append(model_w.wv.similarity('서비스',A[i]))
  B_분위기.append(model_w.wv.similarity('분위기',A[i]))

model_w.wv.similarity('예약','예쁘다')

B_total=pd.DataFrame({'맛있다':B_맛있다,'가격':B_가격,'웨이팅':B_웨이팅,'서비스':B_서비스,'분위기':B_분위기}).transpose()
B_total.columns=[A]

B_total[B_total<0.8]=0

B_total

##단어=문서 행렬 (Term-Document Matrix)
from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()

for i in range(len(X)):
  globals()['val_{}'.format(i)]=[]

B=[]
for i in range(len(X)):
  for j in X[i]:
    if j in A:
      globals()['val_{}'.format(i)].append(j)
      B.append(i)

C=[]
for j in range(len(X)):
  if j not in list(set(B)):
    C.append('')
  else:
    C.append(' '.join(globals()['val_{}'.format(j)]))

C[3]

X[3]

DTM_array=cv.fit_transform(C).toarray()

feature_names=cv.get_feature_names()

DTM_DataFrame=pd.DataFrame(DTM_array,columns=feature_names)

DTM_DataFrame

B_total

##카테고리별 리뷰의 연관성을 알 수 있음
import numpy as np
Result=B_total.to_numpy() @ DTM_DataFrame.transpose().to_numpy()

round(pd.DataFrame(Result),4).to_csv('연관성점수계산_Result_연관성점수.csv')
B_total.to_csv('연관성점수계산_Result_Word2Vec결과.csv')
DTM_DataFrame.to_csv('연관성점수계산_Result_DTM결과.csv')
