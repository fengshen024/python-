from urllib import request
wang_url = 'http://www.renren.com/973643228/profile'

#无代理
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'http://matter.renren.com/',
'Cookie': 'anonymid=k6avsyvwoydlp3; depovince=SD; _r01_=1; JSESSIONID=abc9vv4nAd6-bh5soeBax; ick_login=5cf4738e-39f8-4a16-958e-726f7f5bb6ae; taihe_bi_sdk_uid=e6cc06cd71f60d4b57210ea229075667; taihe_bi_sdk_session=4e4199a88f2b96964ab470dde3c97a0a; t=8dc546e25992e337e183dfa5903277ff8; societyguester=8dc546e25992e337e183dfa5903277ff8; id=973643228; xnsid=e4edbec9; ver=7.0; loginfrom=null; springskin=set; jebe_key=e933016d-17e7-4e37-b0aa-4d68cd87fc6f%7C257b492a9df94560f716381b26ba90e4%7C1581002147527%7C1%7C1581002146305; jebe_key=e933016d-17e7-4e37-b0aa-4d68cd87fc6f%7C257b492a9df94560f716381b26ba90e4%7C1581002147527%7C1%7C1581002146307; vip=1; wp_fold=0; jebecookies=b491857c-1a75-4da2-a661-e7b2893bf6ca|||||; __gads=ID=1b43daeede784979:T=1581002165:S=ALNI_MYb08DwNVhD80kq6dky4hrHNPvzkg'
          }
req = request.Request(url = wang_url,headers=header)
resp = request.urlopen(req)
#print(resp.read().decode('utf-8'))
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))