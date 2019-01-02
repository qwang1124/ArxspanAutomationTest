from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from  selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re,os
import HtmlTestRunner


class TEST_CREATPROJECT_ADMIN(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
    #     self.driver.implicitly_wait(3)


    def test_creat_project_admin(self):
        driver = login()
        driver.maximize_window()
        # time.sleep(3)
        # driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_class_name('newObject').click()
        # time.sleep(3)
        # driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_id('projectName').send_keys('TEST_PROJECT_QW')
        driver.find_element_by_name('projectDescription').send_keys('Test Script execution-01/01/2018')
        driver.find_element_by_name('createProject').click()

        test_value = driver.find_element_by_id('ProjectTitle').text
        print(test_value)
        a = 'TEST_PROJECT_QW'
        test_value2 =driver.find_element_by_id('projectDescription').text
        print(test_value2)
        b = 'Test Script execution-01/01/2018'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_2_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)


def login():
    driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('admin@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver

listaa = 'C:\\Users\\Ms. Wang\Downloads\\arxspan'


def createsuite1():
    testunit=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa,pattern='CreatNotebook_test_admin.py',top_level_dir=None)
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