from urllib import request
from urllib import parse

#不使用代理

# url = 'http://httpbin.org/ip'
# req = request.urlopen(url)
# print(req.read().decode('utf-8'))

#使用代理
handler = request.ProxyHandler({'http':'60.162.67.93:9000'})
opener = request.build_opener(handler)
url = 'http://httpbin.org/ip'
reqs = opener.open(url)
print(reqs.read().decode('utf-8'))