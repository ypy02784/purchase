#-*- coding: UTF-8 -*-
from selenium import webdriver
import datetime
import time
# 将chromedriver放在同一个目录
def buy_on_time(buytime):
  chromedriver = "./chromedriverWin.exe"
  driver = webdriver.Chrome(chromedriver)
  driver.maximize_window()

  driver.get("https://www.taobao.com")
  if driver.find_element_by_link_text("亲，请登录"):
    driver.find_element_by_link_text("亲，请登录").click()
  #留够时间扫码登陆，目前测试密码登陆滑动块会出错，只能手机扫码登陆
  time.sleep(30)
  
  driver.get("https://cart.taobao.com/cart.htm")
  if driver.find_element_by_id("J_SelectAll1"):
    driver.find_element_by_id("J_SelectAll1").click()
  time.sleep(3)
  if driver.find_element_by_link_text("结 算"):
    driver.find_element_by_link_text("结 算").click()
  while True:
    now = datetime.datetime.now()
    if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
      while True:
        try:
         
          driver.find_element_by_link_text('提交订单').click()
        except:
          time.sleep(1)
    time.sleep(0.01)


buy_on_time('2018-11-12 11:40:00')