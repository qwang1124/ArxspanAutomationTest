import time
import unittest

from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class TestCreateexperimentJoe(unittest.TestCase):

    # def test_createexperiment(self):
    #     driver = testjoelogin()
    #     driver.find_element_by_id('createNewExperimentLeftNavButton').click()
    #     select = Select(driver.find_element_by_id('newExperimentNotebookId'))
    #     select.select_by_visible_text('Test_Notebook_QingWang')
    #     select1 = Select(driver.find_element_by_id('newExperimentTypeList'))
    #     select1.select_by_visible_text('Chemistry')
    #     driver.find_element_by_tag_name('button').click()
    #     driver.close()S

    def test_addnote(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235143')
        driver.find_element_by_id('addNoteButton').click()
        # Switch to frame failed

        # driver.switch_to.frame('cke_wysiwyg_frame cke_reset')
        # driver.switch_to.default_content()
        body_string = "TestExperimentNote0109"
        elm = driver.find_element_by_xpath(
            "//body[@class = 'cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        elm.send_keys(body_string)

    #     # elm = driver.find_element_by_class_name('cke_editable cke_editable_themed cke_contents_ltr cke_show_borders')
    #     # elm.send_keys(Keys.TAB)
    #     # elm.click()
    #     # elm.send_keys(u'TestExperimentNote0109')
    #     driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()
    #     driver.find_element_by_id('signExperimentButton').click()
    #     select = Select(driver.find_element_by_id('signStatusBox'))
    #     select.select_by_visible_text('Sign and Close')
    #     select = Select(driver.find_element_by_id('requesteeIdBox'))
    #     select.select_by_visible_text('Jane Biologist')
    #     driver.find_element_by_xpath("//button[contains(@onclick = \'clickSign();\')]").click()

    # upload
    # def test_addfile(self):
    #     driver = testjoelogin()
    #     driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235143')
    #     # driver.find_element_by_id('addFileButton').click()
    #     # elm = driver.find_element_by_xpath("//input[@type='file']")
    #     # elm.send_keys('C:\\Users\\QingW\\Downloads\\fwdtestscriptsandtestingfiles\\06epoxideopening.cdx')
    #     # time.sleep(2)
    #     # driver.find_element_by_class_name('resumableUploadButton').click()
    #
    #     driver.find_element_by_id('uploadReaction').click()
    #     driver.find_element_by_id('rxnFile').send_keys('C:\\Users\\QingW\\Downloads'
    #                                                    '\\fwdtestscriptsandtestingfiles\\06epoxideopening.cdx')
    #     time.sleep(2)
    #     driver.find_element_by_xpath("//button[contains(@onclick, 'rxnFile')]").click()

        # driver.find_element_by_id('addFile_tab').click()
        # driver.find_element_by_id('resumableFile1').click()
        # time.sleep(2)
        # driver.find_element_by_id('resumableActualFileName').send_keys('C:\\Users\\Ms. Wang\\Downloads\\arxspan'
        #                                                                '\\Alports Histology Analysis')
        # time.sleep(2)
        # driver.find_element_by_class_name('resumableUploadButton').click()
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


listaa = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\ArxspanAutomationTest'


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
filename = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports\\result.html'
fp = open(filename, 'wb')
filepath = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports'

runner = HTMLTestRunner(output=filepath)
# runner = HTMLTestRunner()

runner.run(createsuite1())

fp.close()
