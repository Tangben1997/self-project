from urllib import request,parse

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8D%97%E4%BA%AC&needAddtionalResult=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'referer': 'https://www.lagou.com/jobs/list_Java?px=default&city=%E5%8D%97%E4%BA%AC'
}

data = {
  'first':'true',
    'pn':'1',
    'kd':'java'
}
req = request.Request(url,headers=headers,data = parse.urlencode(data).encode('utf-8'),method='POST')
reqs = request.urlopen(req)
print(reqs.read().decode('utf-8'))
