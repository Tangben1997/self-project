from urllib import request

url = 'http://www.renren.com/880151247/profile'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':'anonymid=jy9pj1vve2ioe4; depovince=GW; _r01_=1; JSESSIONID=abcaw4yVcyyscgQUo3iWw; ick_login=e168c71e-9539-4ece-8ba4-a95608f09469; __utma=151146938.385594333.1563516798.1563516798.1563516798.1; __utmc=151146938; __utmz=151146938.1563516798.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ick=631a730a-362c-418a-8ac7-39627687e75e; t=ab17545338c9ac094654c3108d2890f10; societyguester=ab17545338c9ac094654c3108d2890f10; id=971544930; xnsid=f7216921; XNESSESSIONID=66ed90e49943; ver=7.0; loginfrom=null; jebe_key=9baac861-d506-4ae7-bcbf-b7094f0df507%7Cf209f3dd9362ea7cedd3b355a2a196c8%7C1563517029113%7C1%7C1563517029378; wp_fold=0; jebecookies=20aed7e4-aeb2-4a0b-9609-38928def4836|||||',
    'Referer':'http://www.renren.com/971544930/newsfeed/photo'
}

req = request.Request(url=url,headers=headers)
resp = request.urlopen(req)
with open('renren.html','w',encoding='utf-8') as fd:
    fd.write(resp.read().decode('utf-8'))