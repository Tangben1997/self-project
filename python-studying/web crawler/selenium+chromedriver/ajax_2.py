#driver.close()关闭页面
#driver.quit()关闭浏览器

from selenium import webdriver
import time

driver_path = r'/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
time.sleep(5)
driver.quit()