# _*_coding:utf-8_*_  
from selenium import webdriver
import datetime  
import time
import os


driver = webdriver.Chrome(executable_path="./chromedriverMAC")

def login(uname, pwd):
    driver.get("http://www.jd.com")
    time.sleep(1)
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(1)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(10)#此处留十秒用于人操作进行滑块验证
    # driver.get("https://sale.jd.com/act/fxsPg3pquZ.html")

    # driver.find_element_by_link_text("去结算").click()
    # now = datetime.datetime.now()
    # print('login success:',now.strftime('%Y-%m-%d %H:%M:%S'))


# buytime = '2016-12-27 22:31:00' 
def buy_on_time(buytime,quan_link):
    
       
    pre = datetime.datetime.strptime(buytime, '%Y-%m-%d %H:%M:%S') - datetime.timedelta(seconds=40)
    pre = pre.strftime('%Y-%m-%d %H:%M:%S')

    while True:   
      now = datetime.datetime.now()  
      if pre == now:
        driver.refresh()
      if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:#因该提前一秒刷新，可以考虑毫秒刷新
            
        driver.get(quan_link)
        time.sleep(0.01)
        
#test

#自动登录，输入用户名和密码
login('ypy02784@163.com', 'ypy19840525')
#自动抢券设定，抢券时间及优惠券地址,时间必须写成00：00：00格式，否则不匹配
buy_on_time('2018-11-14 19:59:58','https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=297e27e0b46c4af69b2abe915a9ddf27&roleId=15012289&to=sale.jd.com/act/fpgmdSRPst.html&cpdad=1DLSUE')
