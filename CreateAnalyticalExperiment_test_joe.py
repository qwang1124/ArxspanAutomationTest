import time
import unittest

from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class TestCreateanalyticalexperimentJoe(unittest.TestCase):

    def test_createanalyticalexperiment(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/show-notebooks.asp?id=10715')
        driver.find_element_by_link_text('Analytical Experiment').click()
        driver.find_element_by_id('e_details').send_keys('test')



        driver.find_element_by_id('createNewExperimentLeftNavButton').click()
        select = Select(driver.find_element_by_id('newExperimentNotebookId'))
        select.select_by_visible_text('Test_Notebook_QingWang')
        select1 = Select(driver.find_element_by_id('newExperimentTypeList'))
        select1.select_by_visible_text('Chemistry')
        driver.find_element_by_tag_name('button').click()
        driver.find_element_by_id('e_details').send_keys('test')
        driver.find_element_by_id('uploadReaction').click()
        driver.find_element_by_id('rxnFile').send_keys('C:\\Users\\QingW\\Downloads'
                                                       '\\fwdtestscriptsandtestingfiles\\06epoxideopening.cdx')
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(@onclick, 'rxnFile')]").click()
        driver.close()

        test_value = driver.find_element_by_id('e_name').text
        print(test_value)
        a = 'Test_Notebook_QingWang - 004'
        test_value2 = driver.find_element_by_link_text('Test_Notebook_QingWang - 004').text
        b = 'Test_Notebook_QingWang - 004'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
        picture_name = 'TestCreateexperimentJoe_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
        driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    # addnote: no text insert
    def test_addnote(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235143')
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_element_by_css_selector('body')
        driver.executeScript("arguments[0].innerHTML = 'Set text using innerHTML'", text)
        driver.find_element_by_link_text('Save').click()
        driver.quit()

    #     driver.find_element_by_id('signExperimentButton').click()
    #     select = Select(driver.find_element_by_id('signStatusBox'))
    #     select.select_by_visible_text('Sign and Close')
    #     select = Select(driver.find_element_by_id('requesteeIdBox'))
    #     select.select_by_visible_text('Jane Biologist')
    #     driver.find_element_by_xpath("//button[contains(@onclick = \'clickSign();\')]").click()

    def test_addfile(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235248')
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]').send_keys(
            'C:\\Users\\Ms. Wang\\Downloads\\arxspan'
            '\\nmr ketal reduction2 1H.txt')
        time.sleep(2)
        driver.find_element_by_class_name('resumableUploadButton').click()
        driver.quit()

        test_value = driver.find_element_by_id('e_name').text
        print(test_value)
        a = 'Test_Notebook_QingWang - 004'
        test_value2 = driver.find_element_by_link_text('Test_Notebook_QingWang - 004').text
        b = 'Test_Notebook_QingWang - 004'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
        picture_name = 'TestCreateexperimentJoe_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
        driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)


def testjoelogin():
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


listaa = 'C:\\Users\\Ms. Wang\\Downloads\\ArxspanAutomationTest'


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