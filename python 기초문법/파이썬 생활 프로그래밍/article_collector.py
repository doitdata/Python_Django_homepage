#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, codecs, re, datetime, requests
import urllib.request
from bs4 import BeautifulSoup as bs

url = 'https://news.daum.net/'
f = open(str(datetime.date.today()) + 'article.txt', 'w')
soup = bs(urllib.request.urlopen(url).read(), 'html.parser')

for i in soup.find_all('div', {'class':'thumb_relate'}):
    try:
        f.write(i.text +'\n')
        f.write(i.find_all('a')[0].get('href') + '\n')
        soup2 = bs(urllib.request.urlopen(i.find_all[0].get('href')).read(), 'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass
    
f.close()


# In[ ]:




