from urllib import request,parse
from http.cookiejar import CookieJar

wang_url = 'http://www.renren.com/SysHome.do'
#1.登录
'''
1.1创建cookiejar对象
1.2使用cookiejar创建httpcookieprocess对象
1.3使用hander创建opener
1.4使用opener发送登录请求
'''
cookjar = CookieJar()
hander = request.HTTPCookieProcessor(cookjar)
opener = request.build_opener(hander)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'http://matter.renren.com/'
          }
data ={
    'email':'970138074@qq.com',
    'password':'pythonspider'
}
data
req = request.Request(wang_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
request.urlopen(req)
#fangwen
url_logi = 'http://www.renren.com/973643228/profile'
resp =opener.open(url_logi)
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))
