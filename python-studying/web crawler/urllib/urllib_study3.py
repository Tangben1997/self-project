from urllib import request,parse

url = 'http://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-07-19&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=NJH&purpose_codes=ADULT'

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Rerferer' : 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-07-19&flag=N,N,Y'
}

req = request.Request(url,headers=headers,method='GET')
reqs = request.urlopen(req)
print(reqs.read().decode('utf-8'))