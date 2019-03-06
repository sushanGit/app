#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from appium import webdriver
import tool.isElement as isElement
import tool.back as back

class Ad(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['platformName'] = 'Android'
        desired_caps['autoLaunch'] = 'true'  # Appium是否要自动启动或安装app，默认true
        # desired_caps['version']='8.0.0'
        desired_caps['version'] = '6.0'
        desired_caps['deviceName'] = 'DIG-TL10'  # 这是测试机的型号，可以查看手机的关于本机选项获得
        # desired_caps['deviceName']='STF-AL00'#这是测试机的型号，可以查看手机的关于本机选项获得
        # desired_caps['app'] = PATH('D:\pythonScript\app-debug.apk')#被测试的App在电脑上的位置
        desired_caps['appPackage'] = 'com.mbalib.android.wiki'
        desired_caps['appActivity'] = 'com.mbalib.android.modules.main.app.controller.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)

    # 判断是否有引导图
    def test_aa_layout_iv_bg(self):
        print("引导图")
        ivBg = isElement.find_Element(self, 'id', 'layout_iv_bg')
        if ivBg:
            print("引导图存在")
            # 左滑
            screen = self.get_size()
            num = 1
            while (num <= 4):
                self.driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.05, screen[1] * 0.5, 6000)
                print('第', num, '张引导图')
                num + +1
            self.driver.find_element_by_id('layout_iv_bg').click()
            sleep(5)
        else:
            print("无引导图")

    #闪屏广告点击跳转
    def test_splash_tv_skip(self):
        #判断是否有闪屏广告
        print('判断是否有闪屏广告')
        driver=self.driver
        splash=isElement.find_Element(self,'id','splash_iv_image')
        if splash:
            print('有闪屏广告点击【跳过】')
            driver.find_element_by_id('splash_tv_skip').click()
            Ad.test_is_ad(self)
        else:
            print('test_splash_tv_skip无闪屏广告')

    #不点击跳过闪屏广告，倒计时结束
    def test_noSkip(self):
        print('不点击跳过闪屏广告，倒计时结束')
        # 判断是否有闪屏广告
        driver = self.driver
        splash = isElement.find_Element(self, 'id', 'splash_iv_image')
        #不点击闪屏广告或者跳过按钮，倒计时结束跳转到首页
        if splash:
            print('有闪屏广告不做操作等倒计时')
            sleep(10)
            #判断是否有首页广告
            Ad.test_is_ad(self)
        else:
            print('test_noSkip无闪屏广告')

    #点击闪屏广告
    def test_ad(self):
        #判断是否有更新弹窗
        splash = isElement.find_Element(self, 'id', 'splash_iv_image')
        if splash:
            print('点击闪屏广告')
            self.driver.find_element_by_id('splash_iv_image').click()
            sleep(5)
            #返回
            back.ivBack(self)
            #执行操作：判断是否有闪屏广告
            Ad.test_is_ad(self)
        else:
            print('test_ad无闪屏广告')


    # 判断是否有更新版本弹窗---有点击稍后安装
    def test_ask_tv_cancel(self):
        print('稍后安装用例')
        askTvTitle = isElement.find_Element(self, 'id', 'ask_tv_title')
        if askTvTitle:
            print("存在有更新版本弹窗")
            # 点击【稍后安装】
            self.driver.find_element_by_id('ask_tv_cancel').click()
        else:
            print("不存在有更新版本弹窗")
            sleep(5)

    #立即安装
    def test_ask_tv_confirm(self):
        print('立即安装用例')
        askTvTitle = isElement.find_Element(self, 'id', 'ask_tv_title')
        if askTvTitle:
            print("存在有更新版本弹窗")
            # 点击【立即安装】
            self.driver.find_element_by_id('ask_tv_confirm').click()
        else:
            print("不存在有更新版本弹窗")
            sleep(5)

    #判断是否有好评弹窗
    #def test

    # 判断是否有首页广告
    def test_is_ad(self):
        driver = self.driver
        llparent = isElement.find_Element(self, 'id', 'image')
        sleep(5)
        print('判断是否有首页广告', llparent)
        if llparent:  # 判断是否有首页广告
            print('有首页广告')
            driver.find_element_by_id('image').click()
            sleep(5)
            #返回
            back.ivBack(self)
        else:
            print("无首页广告")
        sleep(5)

    #app轮播图
    def test_home_slideshow(self):
        print('banner图')
        # 判断是否有闪屏广告
        Ad.test_ad(self)
        #判断是否有首页广告
        Ad.test_is_ad(self)
        sleep(5)
        #点击banner
        self.driver.find_element_by_id('bannerContainer').click()
        # 返回
        back.ivBack(self)

    #app首页广告
    def test_home_banner(self):
        print('首页横幅广告')
        # 判断是否有闪屏广告
        Ad.test_ad(self)
        # 判断是否有首页广告
        Ad.test_is_ad(self)
        #判断是否有首页横幅广告
        hengfu=isElement.find_Element(self,'id','iv_home_wiki')
        if hengfu:
            print('存在横幅广告')
            self.driver.find_element_by_id('iv_home_wiki').click()
            back.ivBack(self)
        else:
            print('不存在横幅广告')

    #搜索里的广告
    def test_search_ad(self):
        print('搜索首页广告')
        # 判断是否有闪屏广告
        Ad.test_ad(self)
        # 判断是否有首页广告
        Ad.test_is_ad(self)
        self.driver.find_element_by_id('toolbar_iv_search').click()
        sleep(5)
        #收起键盘
        self.driver.hide_keyboard()
        #点击首个广告：目前是大咖广告
        self.driver.find_elements_by_id("com.mbalib.android.wiki:id/image")[0].click()
        back.ivBack(self)
        #点击每日一词，有句名言，智库早报
        print('进入每日一词')
        self.driver.find_elements_by_id('com.mbalib.android.wiki:id/ivImge')[0].click()
        back.ivBack(self)
        print('进入有句名言')
        self.driver.find_elements_by_id('com.mbalib.android.wiki:id/ivImge')[1].click()
        back.ivBack(self)
        print('进入智库早报')
        self.driver.find_elements_by_id('com.mbalib.android.wiki:id/ivImge')[2].click()
        back.ivBack(self)
        print("进入搜索广告位")
        self.driver.find_elements_by_id("com.mbalib.android.wiki:id/image")[1].click()
        back.ivBack(self)
        #切换到课堂
        print("切换到课堂搜索页")
        self.driver.find_element_by_name('课堂').click()
        #判断是否有广告
        print("判断课堂搜索页是否有广告")
        IvImageAd=isElement.find_Element(self,'id','IvImageAd')
        if IvImageAd:
            print("存在课堂搜索页广告")
            self.driver.find_element_by_id('IvImageAd').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("不存在课堂搜索页广告")

        #切换到资讯搜索页
        print("切换到资讯搜索页")
        self.driver.find_element_by_name('资讯').click()
        IvImageAd = isElement.find_Element(self, 'id', 'IvImageAd')
        if IvImageAd:
            print("存在资讯搜索页广告")
            self.driver.find_element_by_id('IvImageAd').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("不存在资讯搜索页广告")
        sleep(5)

    #大咖开通页背景广告位
    def test_wiki_audio_vip(self):
        print("大咖开通页背景广告位")
        # 判断是否有闪屏广告
        Ad.test_ad(self)
        # 判断是否有首页广告
        Ad.test_is_ad(self)
        #进入大咖首页
        print("点击首页的大咖讲百科进入大咖首页")
        self.driver.find_elements_by_id("com.mbalib.android.wiki:id/ivSection")[0].click()
        #点击开通，进入开通页
        self.driver.find_element_by_id('ll_header').click()
        sleep(5)
        vipAd=isElement.find_Element(self,'id','ivVipBanner')
        if vipAd:
            print("存在大咖开通页背景广告位")
            self.driver.find_element_by_id('ivVipBanner').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("不存在大咖开通页背景广告位")

    #每日一词广告
    def test_dailyword_ad(self):
        print("每日一词广告")
        # 判断是否有闪屏广告
        Ad.test_ad(self)
        # 判断是否有首页广告
        Ad.test_is_ad(self)
        print("进入每日一词")
        self.driver.find_element_by_name('每日一词').click()
        sleep(5)
        #判断是否有广告位
        #先判断每日一词是否是有图
        clImage=isElement.find_Element(self,'id','ivAdImage')
        print("每日一词有广告",clImage)
        if clImage:
            print("每日一词有广告")
            self.driver.find_element_by_id('ivAdImage').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("每日一词无广告")

    #有句名言广告位
    def test_afamous_ad(self):
        print("有句名言广告")
        # 判断是否有闪屏广告
        Ad.test_ad(self)
        # 判断是否有首页广告
        Ad.test_is_ad(self)
        print("进入有句名言")
        self.driver.find_element_by_name('有句名言').click()
        sleep(5)
        # 判断是否有广告位
        # 先判断每日一词是否是有图
        clImage = isElement.find_Element(self, 'id', 'ivAdImage')
        if clImage:
            print("有句名言有广告")
            self.driver.find_element_by_id('ivAdImage').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("有句名言无广告")

    #app课堂首页广告
    def test_ketang_ad(self):
        print("课堂首页广告")
        # 判断是否有闪屏广告
        Ad.test_ad(self)
        # 判断是否有首页广告
        Ad.test_is_ad(self)
        #切换到课堂
        self.driver.find_element_by_name('课堂').click()
        sleep(5)
        #判断是否有弹窗广告
        llparent=isElement.find_Element(self,'id','llparent')
        if llparent:
            print("课堂首页有广告")
            self.driver.find_element_by_id('llparent').click()
            sleep(5)
            back.ivBack(self)
        else:
            print("课堂首页无广告")
        sleep(5)

    def tearDown(self):
        self.driver.quit()