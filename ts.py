
import urllib.request
import get_data


User_Agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
Cookie="s=g011xk5nqc; device_id=9b2b6706f217053333ce12ebb3b3d0e5; bid=058d33393122a2074702e3d5308a8e2d_jghsf9j4; td_cookie=3485456539; __utmz=1.1525917296.35.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.1062585200.1526193537; xq_a_token=961cf015b9bbe883b0ae90285cc49668a927e470; xqat=961cf015b9bbe883b0ae90285cc49668a927e470; xq_r_token=a24e23a6b97e72ce77e446b227336cffd1d90c78; xq_token_expire=Sat%20Jun%2016%202018%2019%3A19%3A03%20GMT%2B0800%20(CST); xq_is_login=1; u=3746657944; aliyungf_tc=AQAAAOr10lqVBA4AsMYPq1JMIiLUmtI3; Hm_lvt_1db88642e346389874251b5a1eded6e3=1527042111,1527057114,1527083077,1527124800; __utmc=1; _gid=GA1.2.977245811.1527133182; snbim_minify=true; __utma=1.347617711.1524823264.1527124800.1527133206.85; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1527135653; _gat_gtag_UA_16079156_4=1"


head_url="https://eth.ppzuida.com/20180427/QU7FclT3/800kb/hls/U1uHIZZ3880"
end_url=".ts"
url=""

#从网上获取数据
def get_data1(url,user_agent,cookie):
    request=urllib.request.Request(url)

    #模拟浏览，添加请求头
    request.add_header("user-agent",user_agent)
    request.add_header("Cookie",cookie)

    #开始请求网址
    response=urllib.request.urlopen(request)
    
    html=response.read()
    #mystr=html.decode("utf-8")
    response.close()

    #返回数据结果
    return html

def save(data,i):
    f=open("视频ts爬取-18-8-17/result/"+str(i)+".ts","wb")
    f.write(data)
    f.close()

for i in range(1,1331,1):
    if i<10:
        url=head_url+"00"+str(i)+end_url
    elif i<100 :
        url=head_url+"0"+str(i)+end_url
    else :
        url=head_url+str(i)+end_url
    
    data=get_data(url,User_Agent,Cookie)

    save(data,i)
    #print(data)

    
    #print(url)



