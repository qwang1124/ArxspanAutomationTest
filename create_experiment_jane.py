from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
import HtmlTestRunner


class TestCreateexperimentJane(unittest.TestCase):

    def test_createexperiment_jane(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/show-notebook.asp?id=10799')
        driver.find_element_by_link_text('Biology Experiment').click()
        driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()

    def test_addexperimentdescription_jane(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/show-notebook.asp?id=10799')
        driver.find_element_by_id('e_details').send_keys('TESTING')
        driver.switch_to.frame(driver.find_element_by_class_name('cke_wysiwyg_frame cke_reset'))
        driver.switch_to.default_content()
        driver.switch_to.frame('cke_wysiwyg_frame cke_reset')
        elm = driver.find_element_by_class_name('cke_editable cke_editable_themed cke_contents_ltr cke_show_borders')
        elm.send_keys(Keys.TAB)
        elm.send_keys(u'TestExperimentNote0109')
        driver.find_element_by_xpath('//a[contains(@onclick = \'clickSave();\')]').click()
        driver.find_element_by_id('signExperimentButton').click()
        select = Select(driver.find_element_by_id('signStatusBox'))
        select.select_by_visible_text('Sign and Close')
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_xpath("//button[contains(@onclick = \'clickSign();\')]").click()


def testjanelogin():
    # driver = webdriver.Chrome('C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver')
    driver = webdriver.Chrome()
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
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

