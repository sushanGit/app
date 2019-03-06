#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from tool import isElement

#广告位链接跳转返回
def ivBack(self):
    iv_back = isElement.find_Element(self, 'id', 'toolbar_iv_back')
    print('判断返回的id：', iv_back)
    if iv_back:
        self.driver.find_element_by_id('toolbar_iv_back').click()
    elif isElement.find_Element(self, 'id', 'iv_back'):
        self.driver.find_element_by_id('iv_back').click()
        print('返回到首页')
    #elif self.driver.find_element_by_name('开通').is_displayed():
        #self.driver.find_element_by_name('取消').click()
    else:
        print('无链接')