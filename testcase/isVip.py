#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from appium import webdriver
import testcase.advertisement as AdTest

#是否为大咖vip
def isVip(self):
    # 判断是否有闪屏广告
    AdTest.Ad.test_ad(self)
    # 判断是否有首页广告
    AdTest.Ad.test_is_ad(self)
    sleep(5)
    print("从首页的【今日推荐】的【大咖讲百科】进入大咖首页")
    self.driver.find_elements_by_id('ivSection')[0].click()
    sleep(5)
    tvDesc=self.driver.find_element_by_id('tvdesc').text
    if tvDesc=='专享大咖讲解':
        print("该用户不是VIP用户")
        return False
    elif tvDesc=="VIP已到期":
        print("该用户VIP已到期")
        return False
    else:
        return True