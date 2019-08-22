import re
import requests

#存放代理信息
Infos=[]
#便利总共10个页面，每次只改动proxylist后面的数字
for i in range(10):
    url = "%s%s%s"%('https://www.kuaidaili.com/ops/proxylist/',str(i+1),'/')
    #请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer':'https://www.kuaidaili.com/ops/'
    }
    #爬去的html页面存放为text
    text = requests.get(url,headers=headers).content.decode('utf-8')
    #正则
    IPs = re.findall(r'<td data-title="IP">(.*?)</td>',text,re.S)
    Ports = re.findall(r'<td data-title="PORT">(.*?)</td>', text, re.S)
    Securitys = re.findall(r'<td data-title="匿名度">(.*?)</td>',text,re.S)
    Types = re.findall(r'<td data-title="类型">(.*?)</td>',text,re.S)
    GorPs = re.findall(r'<td data-title="get/post支持">(.*?)</td>',text,re.S)
    Locations= re.findall(r'<td data-title="位置">(.*?)</td>',text,re.S)
    Speeds= re.findall(r'<td data-title="响应速度">(.*?)</td>',text,re.S)
    TTLs= re.findall(r'<td data-title="最后验证时间">(.*?)</td>',text,re.S)
    #使用zip函数，将之前每一项的第一个放在一起，组成一个info，放在infos里面
    for value in zip(IPs,Ports,Securitys,Types,GorPs,Locations,Speeds,TTLs):
        ip,port,sec,Type,GorP,Local,Speed,TTL=value
        info={
            'IP':ip,
            '端口':port,
            '匿名度':sec,
            '类型':Type,
            '支持协议':GorP,
            '位置':Local,
            '响应速度':Speed,
            '存货时间':TTL
        }
        Infos.append(info)
#文件流写入
with open('免费IP.txt','w',encoding='utf-8') as fp:
        for i in Infos:
            fp.writelines(str(i)+'\n')