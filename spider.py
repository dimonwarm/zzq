#-*- coding: utf-8 -*-，
#encoding = utf-8

import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

url='http://apply.hzcb.gov.cn/apply/app/status/norm/person'
content=urllib2.urlopen(url).read()

soup=BeautifulSoup(content)
issueNumber=soup.find(id='issueNumber')
date_option=issueNumber.findAll('option')

i=0
date=[]
for element in date_option[1:]:
	date.insert(i,element.text)
        i+=1
 
i=0
pagecount=[]
for element in date:	
	data={'pageNo':0,'issueNumber':element,'applyCode':''}
	f=urllib2.urlopen(url,urllib.urlencode(data))
	response=f.read()
	soup2=BeautifulSoup(response)
	jscode=soup2.findAll('script')
	jsstr=str(jscode)
	pagecount.insert(i,int(jsstr[529:533])/16+1)
	i+=1


conn=MySQLdb.Connect(host='localhost',user='root',passwd='danmeng',db='zzq',charset='utf8')
cur=conn.cursor()

j=0
value=[]
for element in date:
	i=1
	date=element[0:4]+"年"+element[4:]+"月"
	while(i<=pagecount[j]):
		data={'pageNo':i,'issueNumber':element,'appyCode':''}
		page=urllib2.urlopen(url,urllib.urlencode(data))
		res=page.read()
		soup3=BeautifulSoup(res)
		li=soup3.findAll('tr','content_data')
		for item in li:
			for td in item:
				if (len(td.string)==13):
					num=str(td.string)
				elif(1<len(td.string)<13):
					name=str(td.string)
			if(num and name):
				value.append((num,name,date))
		cur.executemany('insert into query_result value(%s,%s,%s)',value)
		conn.commit()
		value=[]
		i+=1
	j+=1
			
        
cur.close()
conn.close()
