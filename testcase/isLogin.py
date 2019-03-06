#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from appium import webdriver
import testcase.advertisement as AdTest
import tool.isElement as isElement

def isLogin(self):
    print("判断用户是否登录")
    # 判断是否有闪屏广告
    AdTest.Ad.test_ad(self)
    # 判断是否有首页广告
    AdTest.Ad.test_is_ad(self)
    # 切换到课堂
    self.driver.find_element_by_name('我的').click()
    isLogin=self.driver.find_element_by_id('tvNickName').text
    if isLogin=='点击登录':
        print("用户未登录")
        return False
    else:
        return True