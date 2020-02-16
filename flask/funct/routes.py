from flask import render_template
from funct import funct
import requests
from bs4 import BeautifulSoup

res =requests.get('https://www.hqu.edu.cn/hdxw.htm')

res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
hqunews = []

for i in range(24):
        for news in soup.select('.col_news_list'):
            titles = news.select('font')[i].text
            url = news.select('a')[i]['href']
            hqunews.append({'link':url,'title':titles})

@funct.route('/')
@funct.route('/index')
def func():
    return render_template('index.html',title='HQUNews',hqunews=hqunews)
