##필요한 패키지 설치 및 임포트
"""

!pip3 install beautifulsoup4

import csv
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

"""##망고플레이트 제주도 맛집 링크 수집"""

wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wd.get("https://www.mangoplate.com/top_lists/1095_summerguide_jeju")

post_list = []
title_list=[]

for i in range(1,11):
  ll = wd.find_element(By.XPATH, "//*[@id='contents_list']/ul/li["+str(i)+"]/div/figure/figcaption/div/span/a").get_attribute('href')
  post_list.append(ll)

pageNum = 1

while pageNum < 7:

    element=wd.find_element(By.XPATH, '//*[@id="contents_list"]/div/button')
    wd.execute_script("arguments[0].click();", element)
    time.sleep(1)
    for i in range(pageNum*10+1,pageNum*10+11):
      try:
        ll = wd.find_element(By.XPATH, "//*[@id='contents_list']/ul/li["+str(i)+"]/div/figure/figcaption/div/span/a").get_attribute('href')
        post_list.append(ll)
      except NoSuchElementException:
        print(i)  
    pageNum += 1
    
post_infos = pd.DataFrame({'link':post_list})

post_infos.to_csv('data_공모전_link.csv',index=False)

"""##망고플레이트 제주도 맛집 식당명, 리뷰, 평점, 주소 등등 수집"""

title=[]
review=[]
ID=[]
taste=[]
load=[]
t_1=[] #가고싶다수
t_2=[] #평점

for jj in range(len(post_infos)):
  pageNum=0

  wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  wd.get(post_infos.loc[jj,'link'])
  N=wd.find_element(By.XPATH,'/html/body/main/article/div[1]/div[1]/div/section[3]/header/ul/li[1]/button/span').text

  if int(N)<=5:  
    req = wd.page_source
    soup=BeautifulSoup(req, 'html.parser')
    aa = soup.find_all('p',"RestaurantReviewItem__ReviewText")
    bb= soup.find_all('span','RestaurantReviewItem__RatingText')
    cc=soup.find_all('span','RestaurantReviewItem__UserNickName')
    dd=soup.find('h1','restaurant_name').text
    ee=soup.find('div','Restaurant__InfoItemLabel--RoadAddressText').text
    ff=soup.find('span','cnt favorite').text
    gg=soup.find('strong','rate-point').text

    for i in range(len(aa)):
      review.append(aa[i].text)
      taste.append(bb[i].text)
      ID.append(cc[i].text) 
      title.append(dd)
      load.append(ee)
      t_1.append(ff)
      t_2.append(gg)

  if int(N)%5==0:
    N_1=int(N)//5-1
  else:
    N_1=int(N)//5

  for _ in range(N_1+1):
    element=wd.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[3]/div[2]')
    wd.execute_script("arguments[0].click();", element)
    time.sleep(3)

  req = wd.page_source
  soup=BeautifulSoup(req, 'html.parser')
  aa = soup.find_all('p',"RestaurantReviewItem__ReviewText")
  bb= soup.find_all('span','RestaurantReviewItem__RatingText')
  cc=soup.find_all('span','RestaurantReviewItem__UserNickName')
  dd=soup.find('h1','restaurant_name').text
  ee=soup.find('div','Restaurant__InfoItemLabel--RoadAddressText').text
  ff=soup.find('span','cnt favorite').text
  gg=soup.find('strong','rate-point').text

  for i in range(len(aa)):
    review.append(aa[i].text)
    taste.append(bb[i].text)
    ID.append(cc[i].text) 
    title.append(dd)
    load.append(ee)
    t_1.append(ff)
    t_2.append(gg)

TOTAL = pd.DataFrame({'review':review, 'ID':ID, 'taste':taste, 'title':title,'load':load, '가고싶다':t_1, '평점':t_2})

for i in range(len(TOTAL['review'])-1):
  if TOTAL.loc[i,'review'] in TOTAL.loc[i+1:,'review'].tolist():
    print(TOTAL.loc[i,'review'])

TOTAL.to_csv('크롤링_Result_망고플레이트.csv',index=False)
