from lxml import etree


parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('/home/tbb/PycharmProjects/self-project/python-studying/web crawler/xpath-lxml/ip-proxy.html',parser=parser)
trs = html.xpath('//div[@id="freelist"]/table/tbody/tr')
IPinfos =[]
for tr in trs:
    ip = tr.xpath('./td[1]/text()')[0]
    port = tr.xpath('./td[2]/text()')[0]
    sec = tr.xpath('./td[3]/text()')[0]
    classtype = tr.xpath('./td[4]/text()')[0]
    getpost = tr.xpath('./td[5]/text()')[0]
    loaction = tr.xpath('./td[6]/text()')[0]
    speed= tr.xpath('./td[7]/text()')[0]
    lastconfirmtime = tr.xpath('./td[8]/text()')[0]

    FreeIPinfo ={
        'IP':ip,
        'PORT':port,
        '匿名度':sec,
        '类型':classtype,
        '支持':getpost,
        '位置':loaction,
        '响应速度':speed,
        '确认时间':lastconfirmtime
    }
    IPinfos.append(FreeIPinfo)

for i in IPinfos:
    print(i)

