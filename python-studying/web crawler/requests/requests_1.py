import requests

url='https://www.baidu.com/'
response = requests.get(url)
# print(type(response.text))
# input(">>>>>>")
# print(response.text)
# input(">>>>>>")
# print(type(response.content))
# print(response.content.decode('utf-8'))
#
# input(">>>>>>")
# print(response.url)
# print(response.encoding)
# print(response.status_code)

params = {
    'wd':'中国'
}
url = 'https://wwww.baidu.com/s'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

response = requests.get(url=url,params=params,headers=headers)

print(response.status_code)
print(response.url)
with open('zhongguo.html','w',encoding='utf-8') as fp:
    fp.write(response.text)