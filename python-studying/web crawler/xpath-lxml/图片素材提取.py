import requests
from lxml import etree
from urllib import request

url = 'http://www.imomoe.io/view/7568.html'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Referer':'http://www.imomoe.io/'
}

resp = requests.get(url,headers=headers)
text=resp.content.decode('gbk')

html = etree.HTML(text)
img = html.xpath('//img[@alt="重来吧、魔王大人！"]/@src')[0]
print(img)
request.urlretrieve(img,'1.jpg')