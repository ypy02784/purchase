# _*_coding:utf-8_*_  
from selenium import webdriver
import datetime  
import time


driver = webdriver.Chrome(executable_path="./chromedriverWin")

def login(uname, pwd):
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(1)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(10)#此处留十秒用于人操作进行滑块验证
    # driver.get("https://cart.jd.com/cart.action")

    # driver.find_element_by_link_text("去结算").click()
    # now = datetime.datetime.now()
    # print('login success:',now.strftime('%Y-%m-%d %H:%M:%S'))


# buytime = '2016-12-27 22:31:00' 
def buy_on_time(buytime,quan_link):
    while True:
        now = datetime.datetime.now()
        pre = datetime.datetime.strptime(buytime, '%Y-%m-%d %H:%M:%S') - datetime.timedelta(seconds=40)
        pre = pre.strftime('%Y-%m-%d %H:%M:%S')
        
        if pre == now:
            driver.refresh()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            
            driver.get(quan_link)
            time.sleep(3)
            
            break



   
#test

#自动登录，输入用户名和密码
login('ypy02784@163.com', 'ypy19840525')
#自动抢券设定，抢券时间及优惠券地址
buy_on_time('2018-11-11 23:10:00','https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=89fd337932504e7d80c96e46788d3416&roleId=15676830&to=https://sale.jd.com/mall/hF2HXITYgxb5c0.html')