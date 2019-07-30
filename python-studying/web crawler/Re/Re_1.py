import re
import requests

for i in range(10):
    url = "%s%s%s"%('https://www.kuaidaili.com/ops/proxylist/',str(i+1),'/')
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer':'https://www.kuaidaili.com/ops/'
    }
    text = requests.get(url,headers=headers).content.decode('utf-8')

    IPs = re.findall(r'<td data-title="IP">(.*?)</td>',text,re.S)
    Ports = re.findall(r'<td data-title="IP">(.*?)</td>', text, re.S)
    Securitys = re.findall(r'<td data-title="IP">(.*?)</td>',text,re.S)
    Types = re.findall(r'<td data-title="IP">(.*?)</td>',text,re.S)
    GorPs = re.findall(r'<td data-title="IP">(.*?)</td>',text,re.S)
    Locations= re.findall(r'<td data-title="IP">(.*?)</td>',text,re.S)
    Speeds= re.findall(r'<td data-title="IP">(.*?)</td>',text,re.S)
    TTLs= re.findall(r'<td data-title="最后验证时间">(.*?)</td>',text,re.S)

print(text)
