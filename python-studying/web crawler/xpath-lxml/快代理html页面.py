import requests

url = 'https://www.kuaidaili.com/ops/'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Referer':'https://www.kuaidaili.com/'
}

resp=requests.get(url,headers=headers)
print(resp.content.decode('utf-8'))

with open('/home/tbb/PycharmProjects/self-project/python-studying/web crawler/xpath-lxml/ip-proxy.html','w',encoding='utf-8') as fp:
    fp.write(
        resp.content.decode('utf-8')
    )