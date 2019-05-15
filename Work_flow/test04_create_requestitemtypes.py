import time, re, os
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import platform
from selenium.webdriver.common.action_chains import ActionChains
import allure


class TestCreaterequestitemtypesAdmin(unittest.TestCase):

    @allure.testcase('test_create_requestitemtypes_by_admin')
    def test_create_requestitemtypes_by_admin(self):
        # driver = webdriver.Ie()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://model.arxspan.com/login.asp')
        driver.find_element_by_id('login-email').send_keys('admin@demo.com')
        driver.find_element_by_id('login-pass').send_keys('arxspanLukGood')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        driver.implicitly_wait(10)

        # Create new request item types
        driver.find_element_by_xpath('//*[@id="navOrders"]/li[7]/a').click()
        driver.maximize_window()
        driver.find_elements_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(2) > div.card-header '
                                             '> div > button').click()
        driver.find_elements_by_css_selector('#arxWorkflowContainer > div > div > '
                                             'div.dropdownEditorContainer.requestItemTypesPage.card.makeVisible > '
                                             'div:nth-child(1) > input').send_keys('Q_Testing_requestitemtypes')
        restrictaccess = driver.find_element_by_name('dropdownEditor_restrictAccess_cb')
        restrictaccess.click()
