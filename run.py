#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern="*.py")

if __name__ == "__main__":
    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="本测试报告内容为APP搜索测试")
        runner.run(discover)

