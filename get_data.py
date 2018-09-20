
#theme:get data from web
#data:2018-3-9
#author:Biking
#encoding=utf8

import urllib.request
import simplejson

#从网上获取数据
def get_data(url,user_agent,cookie):
    request=urllib.request.Request(url)

    #模拟浏览，添加请求头
    request.add_header("user-agent",user_agent)
    request.add_header("Cookie",cookie)

    #开始请求网址
    response=urllib.request.urlopen(request)
    
    html=response.read()
    mystr=html.decode("utf-8")
    response.close()

    #转化为json数据结构
    mystr=simplejson.loads(mystr)

    #返回数据结果
    return mystr
