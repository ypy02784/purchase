#-*- coding: UTF-8 -*-
import os
from selenium import webdriver
import datetime
import time
chromedriver = "/Users/ypy/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
def login(uname, pwd):
  # driver.get("https://www.taobao.com")
  driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5f7911d94ZFf0O&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F%3Fspm%3Da1z5k.7633538.0.0.26694c389zspmY")
  # if driver.find_element_by_link_text("亲，请登录"):
  #   driver.find_element_by_link_text("亲，请登录").click()
  # time.sleep(1)
  
  # if driver.find_element_by_link_text("密码登录"):
  #   driver.find_element_by_link_text("密码登录").click()
  # time.sleep(1)
  
  if driver.find_element_by_name("TPL_username"):
    driver.find_element_by_name("TPL_username").send_keys(uname)
  time.sleep(3)
  if driver.find_element_by_name("TPL_password"):
    driver.find_element_by_name("TPL_password").send_keys(pwd)
  time.sleep(3)
  # if driver.find_element_by_id("J_SubmitStatic"):
  #   driver.find_element_by_id("J_SubmitStatic").click()
  # time.sleep(3)
 
  '''driver.get("https://cart.taobao.com/cart.htm")
  if driver.find_element_by_id("J_SelectAll1"):
    driver.find_element_by_id("J_SelectAll1").click()
  time.sleep(3)
  if driver.find_element_by_link_text("结 算"):
    driver.find_element_by_link_text("结 算").click()
  
  
  '''
  now = datetime.datetime.now()
  print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
def buy_on_time(buytime):
  while True:
    now = datetime.datetime.now()
    if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
      while True:
        try:
          driver.find_element_by_link_text('提交订单').click()
        except:
          time.sleep(1)
    time.sleep(0.1)
#中文账号的时候要给它编码一下，不然会出错
login('tb5182805','ypy027849751')
#login("英文账号",'密码')
#buy_on_time('2017-05-06 21:30:01')