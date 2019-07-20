# mainpage:http://www.renren.com/
# dapeng:http://www.renren.com/880151247/profile
# 1.登录
# 1.1创建一个cookiejar对象
from http.cookiejar import CookieJar
from urllib import request, parse

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

def get_opener():
    cookiejar = CookieJar()
    # 1.2使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener
# 1.4使用opener发送登录的请求（人人网的邮箱和密码）
def login_renren(opener):

    data = {
        'email': '9970138074@qq.com',
        'password': 'pythonspider'
    }
    login_url = 'http://www.renren.com/Plogin.do'
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)

def visit_profile(opener):
    # 2.访问个人主页
    dapeng_url = 'http://www.renren.com/880151247/profile'
    # 获得个人主页的页面的时候，不要新建一个opener
    req = request.Request(dapeng_url,headers=headers)
    resp=opener.open(req)
    with open('renren2.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))
if __name__ == '__main__':
    opener=get_opener()
    login_renren(opener)
    visit_profile(opener)
