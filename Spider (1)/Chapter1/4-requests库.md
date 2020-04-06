# 4-requests库

虽然Python的标准库中 urllib模块已经包含了平常我们使用的大多数功能，但是它的 API 使用起来让人感觉不太好，而 Requests宣传是 “HTTP for Humans”，说明使用更简洁方便。

## 安装和文档地址：

利用`pip`可以非常方便的安装：

```
pip install requests
```

中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
github地址：https://github.com/requests/requests

## 发送GET请求：

1. 最简单的发送`get`请求就是通过`requests.get`来调用：

   ```python
   response = requests.get("http://www.baidu.com/")
   ```

2. 添加headers和查询参数：
   如果想添加 headers，可以传入headers参数来增加请求头中的headers信息。如果要将参数放在url中传递，可以利用 params 参数。相关示例代码如下：

   ```python
    import requests
   
    kw = {'wd':'中国'}
   
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
   
    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get("http://www.baidu.com/s", params = kw, headers = headers)
   
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)
   
    # 查看响应内容，response.content返回的字节流数据
    print(response.content)
   
    # 查看完整url地址
    print(response.url)
   
    # 查看响应头部字符编码
    print(response.encoding)
   
    # 查看响应码
    print(response.status_code)
   ```

## 发送POST请求：

1. 最基本的POST请求可以使用`post`方法：

   ```python
   response = requests.post("http://www.baidu.com/",data=data)
   ```

2. 传入data数据：
   这时候就不要再使用`urlencode`进行编码了，直接传入一个字典进去就可以了。比如请求拉勾网的数据的代码：

   ```python
    import requests
   
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0"
   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    }
   
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
   
    resp = requests.post(url,headers=headers,data=data)
    # 如果是json数据，直接可以调用json方法
    print(resp.json())
   ```

## 使用代理：

使用`requests`添加代理也非常简单，只要在请求的方法中（比如`get`或者`post`）传递`proxies`参数就可以了。示例代码如下：

```python
import requests

url = "http://httpbin.org/get"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

proxy = {
    'http': '171.14.209.180:27829'
}

resp = requests.get(url,headers=headers,proxies=proxy)
with open('xx.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)
```

## cookie：

如果在一个响应中包含了`cookie`，那么可以利用`cookies`属性拿到这个返回的`cookie`值：

```python
import requests

url = "http://www.renren.com/PLogin.do"
data = {"email":"970138074@qq.com",'password':"pythonspider"}
resp = requests.get('http://www.baidu.com/')
print(resp.cookies)
print(resp.cookies.get_dict())
```

## session：

之前使用`urllib`库，是可以使用`opener`发送多个请求，多个请求之间是可以共享`cookie`的。那么如果使用`requests`，也要达到共享`cookie`的目的，那么可以使用`requests`库给我们提供的`session`对象。注意，这里的`session`不是web开发中的那个session，这个地方只是一个会话的对象而已。还是以登录人人网为例，使用`requests`来实现。示例代码如下：

```python
import requests

url = "http://www.renren.com/PLogin.do"
data = {"email":"970138074@qq.com",'password':"pythonspider"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

# 登录
session = requests.session()
session.post(url,data=data,headers=headers)

# 访问大鹏个人中心
resp = session.get('http://www.renren.com/880151247/profile')

print(resp.text)
```

## 处理不信任的SSL证书：

对于那些已经被信任的SSL整数的网站，比如`https://www.baidu.com/`，那么使用`requests`直接就可以正常的返回响应。示例代码如下：

```python
resp = requests.get('http://www.12306.cn/mormhweb/',verify=False)
print(resp.content.decode())
```