
import requests
print('***************')
#response = requests.get('https://www.baidu.com/s')
#print(type(response.text))解码
#print(type(response.content))未解码
#print(response.text)
#print(response.content.decode('utf-8'))可以自己解码
#print(response.url)
#print(response.encoding)头部字符编码
#print(response.status_code)返回响应值
print('***************')
params = {
    'wd':'中国'
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
res = requests.get('https://www.baidu.com/s',params=params, headers = headers)
print(res.url)

with open('baidu.html','w',encoding='utf-8') as fb:
    fb.write(res.content.decode('utf-8'))


# import requests
#
# baseurl = 'http://tieba.baidu.com/f?'
# params = {
#   'kw' : '赵丽颖吧',
#   'pn' : '50'
# }
# headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
# # 自动对params进行编码,然后自动和url进行拼接,去发请求
# res = requests.get(baseurl,params=params,headers=headers)
# res.encoding = 'utf-8'
# print(res.text)