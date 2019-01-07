from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
import HtmlTestRunner


class TestCreateexperimentJoe(unittest.TestCase):

    def test_createexperiment(self):
        driver = testjoelogin()
        driver.find_element_by_id('createNewExperimentLeftNavButton').click()
        select = Select(driver.find_element_by_id('newExperimentNotebookId'))
        select.select_by_visible_text('Test_Notebook_QingWang')
        select1 = Select(driver.find_element_by_id('newExperimentTypeList'))
        select1.select_by_visible_text('')
        driver.find_element_by_tag_name('button').click()
        driver.find_element_by_id('addFile_tab').click()
        driver.find_element_by_id('resumableFile1').click()
        time.sleep(2)
        driver.find_element_by_id('resumableActualFileName').send_keys('C:\\Users\\Ms. Wang\\Downloads\\arxspan'
                                                                       '\\Alports Histology Analysis')
        time.sleep(2)
        driver.find_element_by_class_name('resumableUploadButton').click()
        # upload.get_attribute('value')

        driver.quit()

        # test_value = driver.find_element_by_id('NotebookTitle').text
        # print(test_value)
        # a = 'Test_Notebook_QingWang'
        # test_value2 = driver.find_element_by_id('notebookOwnerSpan').text
        # b = 'System Administrator'
        # test_value3 =driver.find_element_by_id('notebookDescription').text
        # print(test_value2)
        # c = 'Test Script execution-01/01/2019'
        #
        # if a in test_value and b in test_value2 and c in test_value3:
        #     valid = True
        # else:
        #     valid = False
        #     picture_name = 'test_CreateNotebookAdmin_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
        #     driver.get_screenshot_as_file(picture_name)
        # self.assertTrue(valid)


def testjoelogin():
    # driver = webdriver.Chrome('C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver')
    driver = webdriver.Chrome()
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver


listaa = 'C:\\Users\\Ms. Wang\\Downloads\\ArxspanAutomation\\ArxspanAutomationTest-master'


def createsuite1():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='create_experiment_joe.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


currenttime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
reportfile = 'ResultReport' + currenttime + '.html'
filename = 'C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\reports\\result.html'
fp = open(filename, 'wb')
filepath = 'C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\reports'

runner = HTMLTestRunner(output=filepath)
# runner = HTMLTestRunner()

runner.run(createsuite1())

fp.close()
