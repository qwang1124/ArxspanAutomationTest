#!/usr/bin/python
# -*- coding: utf-8 -*-
# Test ID: test-01
# Test name: Login Test
# Expect output: Login successful
# Step description:
#      1. Open the Chrome driver;
#      2. Launch the URL of login page;
#      3. Input the Joe as the username;
#      4. Input the password;
#      5. Choose the different company;
#      6. Successfully login
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os


class TEST_Login_Jane(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
        self.driver.implicitly_wait(3)
        self.base_url = "https://model.arxspan.com/login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_company_demo(self):
        driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
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
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Demo'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_Demo_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    def test_company_CpdTrackingNoInv(self):
        driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('CpdTrackingNoInv')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'CpdTrackingNoInv'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_CpdTrackingNoInv_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    def test_company_CTDEMO(self):
        driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('CT DEMO')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'CT DEMO'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_CTDEMO_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    def test_company_DaiichiSankyo(self):
        driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Daiichi Sankyo')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Daiichi Sankyo'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_DaiichiSankyo_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    def test_company_FormulationDemo(self):
        driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Formulation Demo')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Formulation Demo'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_FormulationDemo_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    def test_company_ModelTestScriptCompany(self):
        driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Model Test Script Company'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_ModelTestScriptCompany_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    def test_company_YumanityModel(self):
        driver = webdriver.Chrome("C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Yumanity Model')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Yumanity Model'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_YumanityModel_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)


listaa = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\ArxspanAutomationTest\\login_test'


def createsuite1():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='login_test_Jane.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    currenttime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    reportfile = 'ResultReport' + currenttime + '.html'
    filename = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports\\result.html'
    fp = open(filename, 'wb')
    filepath = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports'

    runner = HTMLTestRunner(output=filepath)

    runner.run(createsuite1())

    fp.close()
