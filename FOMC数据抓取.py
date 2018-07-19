# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 19:37:25 2018

@author: Chang
"""

import requests
import re
header = {
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Cache-Control':'max-age=0',
          'Connection':'keep-alive',
          'Cookie':'',
          'Host':'www.federalreserve.gov',
          'If-Modified-Since':'Fri, 22 Jun 2018 23:25:20 GMT',
          'If-None-Match':'"51d65c4980ad41:0"',
          'Referer':'https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm',
          'Upgrade-Insecure-Requests':'1',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
          }
years = [value for value in range(1936,1960)]
urls = []
for value in years: 
    urls.append("https://www.federalreserve.gov/monetarypolicy/fomchistorical" + str(value) + ".htm")
print(urls)
value_times = []
for url in urls: 
    page = requests.get(url, headers=header)
    pagestr = page.content.decode('utf-8')
    meetings = re.findall('h5>(.*?)</h5>', string=pagestr)
    #print(meetings)
    value_times = value_times + meetings
print(value_times)



#example:2012
page2012 = requests.get("https://www.federalreserve.gov/monetarypolicy/fomchistorical2012.htm", verify=False)
pagestr2012 = page2012.content.decode('utf-8')
meetings2012 = re.findall('<h5 class="panel-heading panel-heading--shaded">(.*?)</h5>', string=pagestr2012)
print(meetings2012)
value_6012 = value_times + meetings2012
#print(value_6012)

#after2012
#headers1319 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#            'Accept-Encoding':'gzip, deflate, sdch, br',
#            'Cache-Control':'max-age=0',
#            'Connection':'keep-alive',
#            'Cookie':'',
#            'Host':'www.federalreserve.gov',
#            'Upgrade-Insecure-Requests':'1',
#            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#           }
#page1319 = requests.get("https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm#7239", headers=headers1319)
#print(page1319)
#pagestr1319 = page1319.content.decode('utf-8')
#month=re.findall('col-md-10 col-lg-(.*?)</div>', string=pagestr1319)
#date=re.findall('<strong>(.*?)</strong></div>', string=pagestr1319)
#print(month)
#html1319 = open(r'C:\Users\Chang\Desktop\Python\FOMC code\html1319.txt','r')
#htmlstr1319 = html1319.content.decode('utf-8')
#month=re.findall('col-md-10 col-lg-(.*?)</div>', string=html1319)
#print(month)