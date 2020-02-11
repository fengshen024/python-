print('*****************')
from urllib import request
from http.cookiejar import MozillaCookieJar
cookiejar = MozillaCookieJar("cook.txt")
cookiejar.load()#上传文件cookie
hander = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(hander)
resp = opener.open('http://www.baidu.com')
cookiejar.save(ignore_discard=True)#过期也可以存