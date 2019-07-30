from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=device-width,initial-scale=1.0, maximum-scale=1.0,minimum-scale=1.0,user-scalable=no" />
<title>开放代理 - 快代理</title>

<meta name="keywords" content="开放代理,代理IP,http代理,代理ipapi,https代理服务器,刷单代理ip,爬虫代理ip,国内代理服务器,高速代理服务器," />
<meta name="description" content="开放代理是我们在公网上收集的代理服务器，数量超百万，通过高并发检测，在任何时间都能筛选出实时可用的代理IP，提供强大的API接口。" />

<meta content="index,follow" name="robots"/>
<meta content="index,follow" name="GOOGLEBOT"/>
<meta content="快代理"  name="Author"/>
<meta name="renderer" content="webkit" />
<meta name="baidu_union_verify" content="c087a423b52225f404d4c97e59e53464">
<meta name="google-site-verification" content="Pd8y4Id4xJSxMvj-OwUhaZaK7COpr-8LcANUG30jxW8" />
<link rel="shortcut icon" href="https://img.kuaidaili.com/img/favicon.ico?v=3" type="image/x-icon">


<link rel="stylesheet" href="https://img.kuaidaili.com/css/all.css?v=87" media="screen" />

<style>
</style>


<meta name="renderer" content="webkit">
<meta name="baidu-site-verification" content="AO3Q6dKj9R" />
<meta name="baidu-site-verification" content="1flUdvqxyo" />
<meta name="sogou_site_verification" content="9ELczs5cQc"/>
<meta name="360-site-verification" content="feeadcad97dd7093f9abb1ee5285f031" />
<meta baidu-gxt-verify-token="0fd36d429c039b254364ec1f35f82358">
</head>

<body>
<div class="body">
<!--notify-->
<div id="top_notify"></div>


<!--start header-->

    <!--PC header-->
    <div id="navigationBar" class="topnav topnav-has" style="z-index: 1000;">
        <div class="navigation-inner">
            <div class="logo">
                <h1>
                    <a href="/" class="logo-img">
                        <img class="logo-lit" src="https://img.kuaidaili.com/img/kdl-logo.png" alt="">
                    </a>
                </h1>
            </div>
            <div class="categories" id="nav-con">
                <ul class="menu">
                    <li id="menu_free" class="presentation">
                        <h2><a href="/free/">免费代理</a></h2>
                    </li>
                    
                    <li id="menu_pricing" class="presentation">
                        <h2><a href="/pricing/">购买代理</a></h2>
                    </li>
                    <li id="menu_dps" class="presentation has-menu">
                        <h2><a href="/dps/">私密代理</a></h2>
                    </li>
                    <li id="menu_kps" class="presentation">
                        <h2><a href="/kps/">独享代理</a></h2>
                    </li>
                    <li id="menu_ops" class="presentation">
                        <h2><a href="/ops/">开放代理</a></h2>
                    </li>
                    <li id="menu_fetch" class="presentation has-menu">
                        <h2><a href="/fetch/">代理提取</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="/fetch/">提取开放代理</a></li>
                                <li><a href="/dps/fetch/">提取私密代理</a></li>
                                <li><a href="/kps/fetch/">提取独享代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_apidoc" class="presentation has-menu">
                        <h2><a href="https://help.kuaidaili.com/api/intro/" target="_blank">API接口</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="https://help.kuaidaili.com/api/intro/" target="_blank">API文档</a></li>
                                <li><a href="https://help.kuaidaili.com/dev/intro/" target="_blank">开发指南</a></li>
                                <li><a href="https://help.kuaidaili.com/dev/sdk/" target="_blank">SDK下载</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_help" class="presentation has-menu">
                        <h2><a href="https://help.kuaidaili.com" target="_blank">帮助中心</a></h2>
                    </li>
                </ul>
            </div>
            <div class="operation">
                <span class="unlogin">
                    <a href="/login/" class="qc-btn link-dl"><span>登录</span></a>
                    <span class="stick">|</span>
                    <a href="/regist/" class="qc-btn link-dl"><span>注册</span></a>
                </span>
                <a href="/usercenter/" class="qc-btn link-name welcome-link"><span class="welcome"></span></a>
                <a href="/usercenter/" class="qc-btn link-mc"><span>会员中心</span></a><span id="noti"></span>
            </div>
        </div>
    </div>

    <!--mobile header-->
    <div id="navigationMobileBar" class="topnav-m topnav-m-has" style="z-index: 101;">
        <div class="navigation-inner" id="navDefault" style="transition: left 0s ease-in-out; transform: translateZ(0px); position: absolute; width: 100%; left: 0px;">
            <div class="navigation-bar m-nav-1" id="navigation-bar">
                <div class="area-left">
                    <div class="logo">
                        <h1>
                            <a href="/" class="logo-img">
                                <img class="logo-lit" src="https://img.kuaidaili.com/img/kdl-logo.png" alt="">
                                <img class="logo-dark" src="https://img.kuaidaili.com/img/kdl-logo.png" alt="">
                            </a>
                        </h1>
                    </div>
                </div>
                <div class="area-right">
                    <a href="javascript:;" class="nav-mobile-button m-more">
                        <span class="button-img"></span>
                    </a>
                    <a href="javascript:;" class="nav-mobile-button m-close">
                        <span class="button-img"></span>
                    </a>
                </div>
            </div>
            <div class="categories-mobile" id="navDefaultSub" style="opacity: 0; transition: opacity 0.4s ease-in-out; transform: translateZ(0px); display: none;">
                <ul id="m_top_menu" class="menu">
                    <li class="presentation nav-right"><h2><a href="/free/">免费代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/pricing/">购买代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/dps/">私密代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/kps/">独享代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/ops/">开放代理</a></h2></li>
                    <li class="presentation nav-down">
                        <h2><a href="javascript:void(0);">代理提取</a></h2>
                        <div class="nav-down-menu" style="display: none;">
                            <ul class="nav-down-menu-detail">
                                <li><a class="title" href="/fetch/">提取开放代理</a></li>
                                <li><a class="title" href="/dps/fetch/">提取私密代理</a></li>
                                <li><a class="title" href="/kps/fetch/">提取独享代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="presentation nav-down">
                        <h2><a href="https://help.kuaidaili.com/api/intro/" target="_blank">API接口</a></h2>
                    </li>
                    <li class="presentation nav-right"><h2><a href="https://help.kuaidaili.com" target="_blank">帮助中心</a></h2></li>
                </ul>
                <ul class="op">
                    <li><a href="/usercenter/" class="op-btn btn-style-2">会员中心</a></li>
                </ul>
                <div class="sign-in">
                    <a href="/usercenter/" class="sign-in-links welcome-link"><span class="welcome"></span></a>
                    <span class="unlogin">
                        <a id="m_login_btn" href="/login/" class="sign-in-links">登录</a>
                        <span class="stick">|</span>
                        <a id="m_opt_btn" href="/regist/" class="sign-in-links">注册</a>
                    </span>
                </div>
                <div class="contact">
                    <a href="tel:4000580638" class="ct-num">
                        <i class="icon"></i>
                        <span>400-058-0638</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

<!--end header-->


<div id="content">

    <div class="kf-banner content-fs">
        <div class="con-body">
            <div class="kf-banner-text">
                <h2 class="title">开放代理</h2>
                <p class="context">开放代理是从公网收集的开放代理服务器，每天可用IP超过30000个，大部分IP可用时间在10分钟以内。使用API接口可以方便地嵌入您的程序和软件中。</p>
                <a href="/pricing/#ops" class="blue-btn">立即选购</a>
            </div>
        </div>
    </div>

    <div class="content-fs mod-wrap mod-wrap-subnav">
        <div class="con-body">
            <ul class="sub-nav" style="">
                <li><a href="." class="active">开放代理概览</a></li>
                <li><a href="https://help.kuaidaili.com/product/ops/" target="_blank">产品详细信息</a></li>
                <li><a href="/pricing/#ops">定价</a></li>
                <li><a href="https://help.kuaidaili.com/dev/intro/" target="_blank">入门指南</a></li>
                <li><a href="https://help.kuaidaili.com/api/intro/" target="_blank">API接口</a></li>
                <li><a href="https://help.kuaidaili.com/dev/sdk_http/" target="_blank">代码样例</a></li>
                <li><a href="https://help.kuaidaili.com/dev/sdk/" target="_blank">SDK下载</a></li>
            </ul>
        </div>
    </div>

    <div class="m-padding13 sm-table-gray about-sec">
        <div class="con-body">
            <div class="about-mod-con">
                <div class="about-c-horiz about-intro">
                    <div class="about-c-img">
                        <img src="https://img.kuaidaili.com/img/product-logo03.png" alt="">
                    </div>
                    <div class="about-c-body">
                        <h4 class="about-c-heading">开放代理简介</h4>
                        <div class="about-c-info">
                            <p class="sec">
                                开放代理是从公网收集的代理服务器，具有IP数量大，使用成本低的特点。<br/>
                                得益于我们高效的分布式代理收集系统，和高并发的规模化处理能力，每小时超过百万的代理被检测和更新，使得全年在超过80%的时间都能有10000个以上的代理IP可供提取使用。<br/>
                                开放代理使用非常方便，只需几分钟，您就可以通过<a href="https://help.kuaidaili.com/api/getproxy/" target="_blank">API接口</a>获取代理IP并参照<a href="https://help.kuaidaili.com/dev/sdk_http/" target="_blank">代码样例</a>集成到您的程序中，您也可以<a href="/genapiurl/" target="_blank">在线生成API链接</a>内置到软件中使用。<br/>
                                <a class="more" href="https://help.kuaidaili.com/product/ops/" target="_blank">了解详情 &gt;&gt;</a>
                            </p>
                        </div>
                        
                    </div>
                </div>
                <div class="about-event">
                    <div class="about-event-tit">
                        活动 &amp; 公告
                    </div>
                    <div class="about-event-con">
                        <ul>
                            <li class="about-event-item">
                                <i class="event-block-icon">试用</i>
                                <a class="online-chat" href="javascript:void(0);">
                                    开放代理所有产品提供4小时免费测试，请联系客服开通试用 &gt;&gt;
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
                
            </div>
        </div>
    </div>

    <div class="m-padding12">
        <div class="con-body">
            <div class="kf-table">
                <h2 class="title title2">开放代理的特点</h2>
                <table class="descr">
                  <thead class="center">
                    <tr>
                        <td width="20%">优势</td>
                        <td width="80%">为什么使用快代理开放代理</td>
                    </tr>
                  </thead>
                  <tbody class="center">
                    <tr>
                        <td data-title="优势" class="shu-title">及时收集</td>
                        <td data-title="为什么使用快代理开放代理" class="shu-text">高效、精准的公网代理收集系统7x24小时运行，每天扫描的代理数以万计，最新出现的代理总能在第一时间收录。</td>
                    </tr>
                    <tr>
                        <td data-title="优势" class="shu-title">精确检测</td>
                        <td data-title="为什么使用快代理开放代理" class="shu-text">精确检测每一个代理IP的匿名度、响应时间、数据传输速度、地域、运营商，平均每个IP每天被检测上百次，因此您总是可以在这里找到可以正常工作的代理。</td>
                    </tr>
                    <tr>
                        <td data-title="优势" class="shu-title">智能筛选</td>
                        <td data-title="为什么使用快代理开放代理" class="shu-text">持续检测每一个代理IP的存活和消亡数据，根据一定的算法智能筛选出稳定的IP，可用率大大高于平均水平。</td>
                    </tr>
                    <tr>
                        <td data-title="优势" class="shu-title">强大的API</td>
                        <td data-title="为什么使用快代理开放代理" class="shu-text">筛选支持https和post的代理，匿名度、地区、运营商、响应速度、端口号、ip段筛选，返回结果支持json／xml格式，支持提取结果排序。</td>
                    </tr>
                  </tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="content-fs kf-numBanner">
        <div class="con-body">
            <div id="ip_realtime" class="kf-bannerBox">
                <p class="title">实时可用代理<i class="kf-tabmp"><br></i><span>11092</span>个</p>
                <p class="content">22秒前更新</p>
                <a href="/dist/" class="look-where">点击查看实时分布</a>
            </div>
        </div>
    </div>

  
    <div class="m-padding12">
        <div class="con-body">
            <div id="ip_stat" class="kf-table">
                <h2 class="title title2">单日代理数量统计</h2>
                <table class="table table-b table-bordered table-striped">
                  <thead class="center">
                    <tr>
                        <th>http代理</th>
                        <th>https代理</th>
                        <th>高匿名代理</th>
                        <th>高匿名https代理</th>
                        <th>高匿名稳定代理</th>
                        <th>高匿名https稳定代理</th>
                    </tr>
                  </thead>
                  <tbody class="center">
                    <tr>
                        <td data-title="http代理">36630<span class="unit">个</span></td>
                        <td data-title="https代理">29379<span class="unit">个</span></td>
                        <td data-title="高匿名代理">25665<span class="unit">个</span></td>
                        <td data-title="高匿名https代理">21326<span class="unit">个</span></td>
                        <td data-title="高匿名稳定代理">3332<span class="unit">个</span></td>
                        <td data-title="高匿名https稳定代理">2900<span class="unit">个</span></td>
                    </tr>
                  </tbody>
                </table>
                <p class="data-tips">数据来源：昨天全天（2019-07-23）</p>
            </div>

            <div class="kf-table">
                <h2 class="title title2">多日代理数量统计</h2>
                <table class="table table-b table-bordered table-striped">
                  <thead class="center">
                    <tr>
                        <th width="14%">昨天累计可用</th>
                        <th width="9%">过去3天累计可用</th>
                        <th width="9%">过去7天累计可用</th>
                        <th width="13%">过去15天累计可用</th>
                    </tr>
                  </thead>
                  <tbody class="center">
                    <tr>
                        <td data-title="昨天累计可用">36630<span class="unit">个</span></td>
                        <td data-title="过去3天累计可用">49022<span class="unit">个</span></td>
                        <td data-title="过去7天累计可用">59598<span class="unit">个</span></td>
                        <td data-title="过去15天累计可用">85722<span class="unit">个</span></td>
                    </tr>
                  </tbody>
                </table>
                <p class="data-tips">注：数据统计以昨天为基准（2019-07-23）</p>
            </div>
        </div>
    </div>
  

    <div class="m-padding12">
        <div class="con-body">
            <div id="freelist" class="kf-table">
                <h2 class="title title2">免费高速HTTP代理IP列表（2019-07-24）</h2>
                <table class="table table-b table-bordered table-striped">
                  <thead class="center">
                    <tr>
                        <th width="14%">IP</th>
                        <th width="9%">PORT</th>
                        <th width="9%">匿名度</th>
                        <th width="13%">类型</th>
                        <th width="12%">get/post支持</th>
                        <th width="21%">位置</th>
                        <th width="10%">响应速度</th>
                        <th width="12%">最后验证时间</th>
                    </tr>
                  </thead>
                  <tbody class="center">
                    
                    <tr>
                        <td data-title="IP">118.24.156.214</td>
                        <td data-title="PORT">8118</td>
                        <td data-title="匿名度">高匿名</td>
                        <td data-title="类型">HTTP, HTTPS</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">中国 四川 成都 电信</td>
                        <td data-title="响应速度">2秒</td>
                        <td data-title="最后验证时间">1分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">36.26.154.125</td>
                        <td data-title="PORT">3128</td>
                        <td data-title="匿名度">匿名</td>
                        <td data-title="类型">HTTP</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">中国 浙江 衢州 电信</td>
                        <td data-title="响应速度">1秒</td>
                        <td data-title="最后验证时间">4分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">180.118.86.243</td>
                        <td data-title="PORT">9000</td>
                        <td data-title="匿名度">匿名</td>
                        <td data-title="类型">HTTP</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">中国 江苏 镇江 电信</td>
                        <td data-title="响应速度">2秒</td>
                        <td data-title="最后验证时间">7分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">163.125.31.12</td>
                        <td data-title="PORT">8118</td>
                        <td data-title="匿名度">高匿名</td>
                        <td data-title="类型">HTTP, HTTPS</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">中国 广东 深圳 联通</td>
                        <td data-title="响应速度">1秒</td>
                        <td data-title="最后验证时间">10分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">106.14.160.134</td>
                        <td data-title="PORT">80</td>
                        <td data-title="匿名度">高匿名</td>
                        <td data-title="类型">HTTP, HTTPS</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">上海市上海市 阿里云计算有限公司 阿里云</td>
                        <td data-title="响应速度">1秒</td>
                        <td data-title="最后验证时间">13分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">47.100.21.174</td>
                        <td data-title="PORT">8021</td>
                        <td data-title="匿名度">高匿名</td>
                        <td data-title="类型">HTTP, HTTPS</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">上海市上海市  阿里云</td>
                        <td data-title="响应速度">2秒</td>
                        <td data-title="最后验证时间">16分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">114.235.23.154</td>
                        <td data-title="PORT">9000</td>
                        <td data-title="匿名度">高匿名</td>
                        <td data-title="类型">HTTP</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">江苏省徐州市  电信</td>
                        <td data-title="响应速度">1秒</td>
                        <td data-title="最后验证时间">19分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">118.24.127.144</td>
                        <td data-title="PORT">1080</td>
                        <td data-title="匿名度">匿名</td>
                        <td data-title="类型">HTTP, HTTPS</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">中国 四川 成都 电信</td>
                        <td data-title="响应速度">3秒</td>
                        <td data-title="最后验证时间">22分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">140.143.6.16</td>
                        <td data-title="PORT">1080</td>
                        <td data-title="匿名度">匿名</td>
                        <td data-title="类型">HTTP, HTTPS</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">中国 天津 天津 电信</td>
                        <td data-title="响应速度">3秒</td>
                        <td data-title="最后验证时间">25分钟前</td>
                    </tr>
                    
                    <tr>
                        <td data-title="IP">123.57.84.116</td>
                        <td data-title="PORT">8118</td>
                        <td data-title="匿名度">高匿名</td>
                        <td data-title="类型">HTTP, HTTPS</td>
                        <td data-title="get/post支持">GET, POST</td>
                        <td data-title="位置">中国 北京市 北京市 阿里云</td>
                        <td data-title="响应速度">2秒</td>
                        <td data-title="最后验证时间">28分钟前</td>
                    </tr>
                    
                  </tbody>
                </table>
                <p class="data-tips">注：表中响应速度是中国测速服务器的测试数据，仅供参考。响应速度根据您机器所在的地理位置不同而有差异。</p>

                <div id="listnav">
                    <ul>
                        <li>第</li>
                        <li><a id="p1" href="/ops/proxylist/1/">1</a></li>
                        <li><a id="p2" href="/ops/proxylist/2/">2</a></li>
                        <li><a id="p3" href="/ops/proxylist/3/">3</a></li>
                        <li><a id="p4" href="/ops/proxylist/4/">4</a></li>
                        <li><a id="p5" href="/ops/proxylist/5/">5</a></li>
                        <li><a id="p6" href="/ops/proxylist/6/">6</a></li>
                        <li><a id="p7" href="/ops/proxylist/7/">7</a></li>
                        <li><a id="p8" href="/ops/proxylist/8/">8</a></li>
                        <li><a id="p9" href="/ops/proxylist/9/">9</a></li>
                        <li><a id="p10" href="/ops/proxylist/10/">10</a></li>
                        <li>页</li>
                    </ul>
                </div>

                <div class="btn btn-b center be-f" style="margin-top: 0px;"><a id="tobuy" href="/free/">更多免费代理</a></div>
            </div>

        </div>
    </div>



</div>


<div class="footer">
    <div class="con-body clearfix">
        <div class="footer-left">
            <a href="/" class="logo-link"><img height="35" src="/img/footer-logo.png"/></a>
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a><span>|</span></li>
            <li><a href="/contract/" target="_blank">服务条款</a><span>|</span></li>
            <li><a href="/law/" target="_blank">法律声明</a><span>|</span></li>
            <li><a href="https://img.kuaidaili.com/sitemap.xml">网站地图</a><span>|</span></li>
            <li><a href="https://help.kuaidaili.com/dev/intro/" target="_blank">开发者指南</a><span>|</span></li>
            <li><a href="/changelog/">更新日志</a></li>
            
        </ul>
        <p class="foot-owner">© 2013-2019 积善科技（北京）有限公司<br/>
            <a style="margin-left:0px" href="http://www.miitbeian.gov.cn/publish/query/indexFirst.action" target="_blank">京ICP备16054786号</a>
            <span style="margin-left:6px">增值电信经营许可证 京B2-20181007</span>
            <a style="margin-left:5px" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802027137"><img src="https://img.kuaidaili.com/img/jgwab.png" style="height:18px;vertical-align:sub;" />京公网安备 11010802027137号</a>
        </p>
        </div>
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
          
            <a id='cxwz' class="safe03" href='https://credit.szfw.org/CX20180118037820350186.html' target='_blank'></a>
          
        </div>
    </div>
</div>
<div class="m-footer">
    <div class="con-body">
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a></li>
            <li><a href="https://help.kuaidaili.com/contract/" target="_blank">服务条款</a></li>
            <li><a href="https://help.kuaidaili.com/law/" target="_blank">法律声明</a></li>
            <li><a href="/sitemap.xml">网站地图</a></li>
            <li><a href="https://help.kuaidaili.com" target="_blank">帮助中心</a></li>
            <li><a href="/changelog/">更新日志</a></li>
            
        </ul>
        <p class="foot-owner">©2013-2019&nbsp; 积善科技（北京）有限公司</p>
        <a class="foot-owner" href="http://www.miitbeian.gov.cn/publish/query/indexFirst.action">京ICP备16054786号</a>
        <span class="foot-owner" style="margin-left:5px">增值电信经营许可证 京B2-20181007</span>
        <a class="foot-owner" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802027137"><img src="https://img.kuaidaili.com/img/jgwab.png" style="height:18px;vertical-align:sub;" />京公网安备 11010802027137号</a>
      
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
            <a id='cxwz' class="safe03" href='https://credit.szfw.org/CX20180118037820350186.html' target='_blank'></a>
            
        </div>
      
    </div>
</div>
<div id="mNavMask" style="position: fixed; top: 0px; left: 0px; bottom: 0; right: 0; width: 100%; z-index: 100; height: 100%; display: none; background: rgba(0, 0, 0, 0.74902);"></div>
<ul class="onMShow">
    <li>
        <a class="online-chat" href="javascript:void(0);"><br>
            <span class="bt3"></span>
            <div class="two">客服QQ: 800849628<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="tel:4000580638"><br>
            <span class="bt2"></span>
            <div class="two">客服电话：400-058-0638<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="/support/"><br>
            <span class="bt1"></span>
            <div>提交工单</div>
        </a>
    </li>
</ul>
<a href="javascript:void(0);" id="top_btn" class="label btt" style="display:none;"><span class="btn-top"></span></a>

</div>


<script type="text/javascript" src="https://img.kuaidaili.com/js/all.js?v=38"></script>

<script type="text/javascript">
$("tbody tr:nth-child(even)").addClass("odd");
$(document).ready(function() {
    if(window.location.pathname.indexOf("/proxylist/") != -1)
        jumpToAnchor("freelist");
    $("#p1").addClass("active");
});
</script>

<script type="text/javascript">
var menu = "menu_ops";
if(menu) $('#'+menu).addClass('active');
var ucm = "";
if(ucm){
    $('#ucm_'+ucm).addClass('active');
    $('#ucm_'+ucm+' a i').addClass('icon-white');
}

if(window.location.pathname.lastIndexOf('/usercenter', 0) === 0){
    $('.topnav .navigation-inner').css("max-width", "1400px");
    $('.footer .con-body').css("width", "1380px");
}

(function(){document.getElementById('cxwz').oncontextmenu = function(){return false;}})();

var ie = ieVersion()
if(!ie || ie >= 11){
    loadScript("https://img.kuaidaili.com/js/popper-tippy.js", function(){
        if(isDefined(tippy)) {
            tippy.setDefaults({
              arrow: true,
              animation: 'fade',
              duration: [180, 250],
              theme: 'light-border'
            })
        }

    });
}
</script>

<script type="text/javascript">
var chat_url = "https://static.meiqia.com/dist/standalone.html?_=t&eid=72194";
$(document).ready(function() {
    init_chat();
});
</script>

<script type="text/javascript">
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?7ed65b1cc4b810e9fd37959c9bb51b31";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://img.kuaidaili.com/ga/ga.js','ga');
ga('create', 'UA-76097251-1', 'auto');
ga('send', 'pageview');
</script>


<!--[if lt IE 9]><link rel="stylesheet" href="https://img.kuaidaili.com/css/ie.css?v=10" media="screen" /><![endif]-->
</body>
</html>
"""
soup = BeautifulSoup(html,"lxml")

# #获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('===')

#获取第二个tr标签