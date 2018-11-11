# _*_coding:utf-8_*_  
from selenium import webdriver
import datetime  
import time


driver = webdriver.Chrome(executable_path="/Users/ypy/Downloads/chromedriver")

def login(uname, pwd):
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(1)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(10)#此处留十秒用于人操作进行滑块验证
    driver.get("https://cart.jd.com/cart.action")

    driver.find_element_by_link_text("去结算").click()
    # now = datetime.datetime.now()
    # print('login success:',now.strftime('%Y-%m-%d %H:%M:%S'))


# buytime = '2016-12-27 22:31:00' 
def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            while True:
                try:
                    driver.find_element_by_id('order-submit').click()
                except Exception as e:
                    time.sleep(0.1)
            print ('purchase success',now.strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(0.5)


# entrance
login('ypy02784@163.com', 'ypy19840525')
buy_on_time('2018-11-11 22:10:01')