#用户：xiangjianqun   

#日期：2019-02-25   

#时间：12:05   

#文件名称：PyCharm


#严选数据
import requests
import re

headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
response=requests.get('https://a.yesmywine.com/yanxuan/yanxuan?dts=IN.8.0',headers=headers)
results=response.text
results_new=re.findall('title="(.*?)".*?<li>.*?<li><p>(.*?)</p>.*?<p>('
                       '.*?)</p>.*?<span>(.*?)</span>',
                      results,re.S)


import pandas as pd
df=pd.DataFrame()
a = list(
        results_new)
for i in a:
    i = list(i)
    i = pd.concat([pd.Series(i[0]),pd.Series(i[1].split('：')[1]),pd.Series(i[
                                                                               2].split(
        '：')[1]),
                   pd.Series(i[3])],axis=1)
    df = pd.concat([df , i] , axis=0)
print(df)
df.columns=['品名','好评率','近期销量','价格']
df.to_csv('aa.csv',index=False,encoding='utf-8-sig')