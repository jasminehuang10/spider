#用户：xiangjianqun   

#日期：2019-02-26   

#时间：14:14   

#文件名称：PyCharm

#甄选数据
import requests
import re
path='https://www.yesmywine.com/cms/cmsV1/grandcru/'
url1=path+'gccshop'
url2=path+'2010sales'
url3=path+'youan'
url4=path+'tianbai'
url5=path+'yijizhuang'
url6=path+'finewineworld'
urls=[url1,url2,url3,url4,url5,url6]
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
for url in urls:
    name=urls.index(url)
    name='mingzhuangzhenxuan'+str(name)+'.csv'
    response=requests.get(url,
                      headers=headers,verify=False)
    results=response.text
    results_part1=re.findall('class="prod-img" title="(.*?)".*?class="jr"> <i>('
                       '.*?)</i> <em>('
                       '.*?)</em>.*?<strong>¥<i>(.*?)</i></strong>',
                       results,
                       re.S)
    results_part2=re.findall('class="prod-img" title="(.*?)".*?strong>¥<i>('
                         '.*?)</i></strong>',
                       results,
                       re.S)
    print(results)
    print(results_part1)
    print(results_part2)

    import pandas as pd

    df1=pd.DataFrame()
    df2=pd.DataFrame()
    a = list(results_part1)
    b=list(results_part2)


    def new(result , df):
        a_number = len(result[0])
        for i in result:
            i = list(i)
            x = []
            for j in range(0 , a_number):
                x.append(i[j].strip())
            df = pd.concat([df , pd.Series(x)] , axis=1)
        return df


    df1 = new(a , df1)
    df2 = new(b , df2)
    df1 = df1.T
    df1.columns = ['wine_name' , 'critic' , 'score' , 'price']
    df2 = df2.T
    df2.columns = ['wine_name' , 'price']
    df = pd.merge(left=df2 , right=df1 , how='outer',on='wine_name')
    df.to_csv(name , index=False , encoding='utf-8-sig')