import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd

def gethtml():
    try:
        r = requests.get('https://www.shanghairanking.cn/rankings/bcur/2020')
        r.encoding = r.apparent_encoding
        demo = r.text
        return demo
    except:
        return ""
def totable(html):
    data=pd.DataFrame()
    soup=BeautifulSoup(html,'html.parser')
    temp=soup.find('tbody').children

    for tr in temp:
        tds = tr('td')
        list=[[tds[0].text.strip().replace('\n',''),tds[1].text.strip().replace('\n',''),tds[4].text.strip().replace('\n','')]]
        if(len(list)>0):
            data=data.append(list,ignore_index=True)
    data.columns=['排名','学校名称','总分']
    return data

html=gethtml()
list=[]
data=totable(html)
print(data)
data.to_excel('result.xls',index=False)



