from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
cookiejar.load(ignore_discard=True)
resp = opener.open('http://httpbin.org/cookies/set/tbb/yes')
for cookie in cookiejar:
    print(cookie)
cookiejar.save(ignore_discard=True)
