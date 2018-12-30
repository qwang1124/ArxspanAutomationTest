#!/usr/bin/python
# -*- coding: utf-8 -*-
# Test ID: test-01
# Test name: Login Test
# Expect output: Login successful
# Step description:
#      1. Open the Chrome driver;
#      2. Input the URL of login page;
#      3. Input the Joe as the username;
#      4. Input the password;
#      5. Choose the different company;
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from  selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re,os
import HtmlTestRunner


class TEST2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
        self.driver.implicitly_wait(3)
        self.base_url = "https://model.arxspan.com/login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test2(self):
        driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Demo')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'

        if a in test_value:
            flag =1
        else:
            flag =2
            picture_name = 'test_2_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .jpg'
            driver.get_screenshot_as_file(picture_name)
        self.assertEqual(flag, 1)


# if __name__ == '__main__':
#     html_report_dir = 'html_report'
#     # suite = unittest.TestSuite()
#     # suite.addTest(TEST2('test_2'))
#     # report_name = 'test_2_' + str(time.strftime('%Y%m%d%H%M%S')) + '.html'
#     # rn = open(report_name, 'wb')
#     # runner = HtmlTestRunner.HTMLTestRunner(stream=rn, report_title='report')
#     # runner.run(suite)
#     # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_name))
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))

listaa = 'C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst'


def createsuite1():
    testunit=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa,pattern='test.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename = "C:\\Users\\Ms. Wang\\PycharmProjects\\report\\result.html"
fp = open(filename, 'wb')
filepath = "C:\\Users\\Ms. Wang\\PycharmProjects\\report"
runner = HTMLTestRunner(output=filepath)

runner.run(createsuite1())


fp.close()













