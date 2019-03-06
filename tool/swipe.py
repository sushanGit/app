#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#获取屏幕大小
def get_size(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return (x, y)