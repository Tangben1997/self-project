import os
import re
import time
import requests
from urllib import request
from lxml import etree
import threading
from queue import Queue

#生产者类，生产者负责将斗图啦网站的url解析成图片url和图片名，将这两项存入队列中，生产者类继承了thread线程类
class Producer(threading.Thread):
    #请求头信息，请求头用于伪装成浏览器访问，是最常用的应对反爬虫机制的措施，其中referer是网页依赖源，即表示该请求是从哪一级网页跳转过来的
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Referer': 'http://www.doutula.com/photo/list/?page=1'
    }
    #初始化，主要是传入两个队列，url-q和img-q
    def __init__(self,url_q,img_q,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.url_q = url_q
        self.img_q = img_q
    #run中通过while True循环不断地从url—q中获取网页地址，然后调用analysis解析
    def run(self):
        while True:
            #当url-q队列中所有的地址都被解析完成之后，退出循环（即退出该子线程）
            if(self.url_q.empty()):
                print('url全部解析完成！')
                break
            url = self.url_q.get()
            self.Analysis_page(url)
    #analysis将斗图啦网站的url从url_q队列中读取出来，然后解析成图片名和地址，存入img_q供消费者线程下载
    def Analysis_page(self,url):
            #main中已经访问了一次斗图啦主页，并通过session类保存了这次访问返回的cookie信息，之后调用session的get方法去访问url也会带上上一次访问返回的cookie值
            #这也是防范反爬虫机制的一个手段，即带上cookie，session的get方法实际上和requests方法一致
            text = session.get(url, headers=self.header).text
            #上一步请求获取的网页html存入html变量，调用xpath的解析器去解析
            html = etree.HTML(text)
            #xpath语法获取图片相关信息
            imgs = html.xpath(r'//a[@class="col-xs-6 col-sm-3"]/img[@referrerpolicy="no-referrer"]')
            #title是图片的标题，在标签img下alt属性中，
            for img in imgs:
                title = img.get('alt')
                #这一步主要是命名问题，在操作系统中，一些符号是无法作为文件名的，比如点，问好，星号，会产生歧义，所以用正则将图片名中的一些字符去掉
                name = re.sub(r'[\.\*\?！!。，]', '', title)
                #图片的url，在标签img下的data-original属性中
                href = img.get('data-original')
                #后缀名，图片的后缀名为jpg或者gif，图片的url中有，用splitext方法可以提取
                suffix = os.path.splitext(href)
                filename = name + suffix[1]
                #将解析完的图片名和url存入img队列
                self.img_q.put((href,filename))
#消费者线程负责图片的下载
class Consumer(threading.Thread):
    #类似于生产者，初始化
    def __init__(self,url_q,img_q,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.url_q = url_q
        self.img_q = img_q
    #run方法循环着从img—q中取url和图片名，然后下载
    def run(self):
        while True:
            #如果img和url队列都空了，说明下载完了，退出线程
            if self.url_q.empty()|self.img_q.empty():
                print('全部下载完毕！')
                break
            href,filename = img_q.get()
            #request类的urlretrieve方法可以在输入url和图片存放1路径的情况下直接下载，很方便哦
            request.urlretrieve(href, 'images/' + filename)
            print('下载完成！')


if __name__ == '__main__':
    #创建队列，队列最大值
    url_q = Queue(2500)
    img_q = Queue(500)
    #这里是为了获取cookie，先访问一下那个网站，然后之后用session可以直接带着cookie访问
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Referer': 'http://www.doutula.com/photo/list/?page=1'
    }
    session = requests.session()
    #网站里面点击下一页它的url会在page=后面加1，即用page来区分页码，所以2500页表情页的url的区别就是page的区别
    for x in range(2500):
        url = '%s%s' % ('http://www.doutula.com/photo/list/?page=', str(x + 1))
        #放2500个地址进url队列
        url_q.put(url)
    #先睡一秒，让url队列中有内容了再开始取，不然生产者刚刚开始取的时候发现没有就退出了，线程就会断在那里
    time.sleep(1)
    for i in range(5):
        #实例化生产者线程，开了5个
        t = Producer(url_q,img_q)
        t.start()
        print('%d开始解析'%i)
    #同理，防止生产者还没产出消费者直接就退出了
    time.sleep(1)
    for i in range(5):
        t = Consumer(url_q,img_q)
        t.start()
        print('%d开始下载'%i)



