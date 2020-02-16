###爬虫部分

----

1. 利用requests模块来接收响应的数据包信息（Response[200],成功响应）
2. 利用beautifulsoup来对数据内容进行查找
3. 观察网页特点截取col_news_list以下部分，然后再针对属性去查找出标题和url

````python
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
````

----

###flask部分

----

1. 模块的搭建和组合
2. 模版的用法

----

###nginx反代

----

1. 配置uWSGI

````bash
[uwsgi]
uid = www
gid = www
socket = 127.0.0.1:5000  
master = true
vhost = true
workers = 8
reload-mercy = 10
vacuum = true
max-requests = 10000
limit-as = 1024
buffer-sizi = 3000
pidfile = /var/run/uwsgi.pid
daemonize = /var/log/uwsgi/uwsgi.log  
chdir = /usr/local/web
module = wsgi
chmod-socket = 660
enable-threads = true
````

2. 配置nginx

````bash
server {
        listen       80;
        server_name  www.sample.com;


        location / {
            include  uwsgi_params;
            uwsgi_pass  127.0.0.1:5000;
            uwsgi_param UWSGI_SCRIPT wsgi;
            uwsgi_param UWSGI_CHDIR /usr/local/web;
            index  index.html index.htm;
            client_max_body_size 35m;
        }
}
````

