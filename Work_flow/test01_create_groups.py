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


class TestCreategroupsAdmin(unittest.TestCase):

    @allure.testcase('test_create_groups_by_admin')
    def test_create_groups_by_admin(self):
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

        # Create new workflow manager group, add support and administrator as the member
        driver.find_element_by_css_selector('#navTools > li:nth-child(4) > a').click()
        driver.find_element_by_xpath('//*[@id="topDiv"]/div[1]/span/a').click()
        driver.find_element_by_id('aname').send_keys('Workflow_Manager')
        user = Select(driver.find_element_by_id('auserId_1'))
        user.select_by_visible_text('Arxspan Support')
        driver.find_element_by_id('pGroups_add_endLink').click()
        user = Select(driver.find_element_by_id('auserId_2'))
        user.select_by_visible_text('System Administrator')
        driver.find_element_by_css_selector('#addForm > fieldset > input[type=button]:nth-child(4)').click()

        # Create new CRO group, add Joe as the member
        driver.find_element_by_xpath('//*[@id="topDiv"]/div[1]/span/a').click()
        driver.find_element_by_id('aname').send_keys('CRO one')
        user = Select(driver.find_element_by_id('auserId_1'))
        user.select_by_visible_text('Joe Chemist')
        driver.find_element_by_css_selector('#addForm > fieldset > input[type=button]:nth-child(4)').click()

        # Create new internal research group, add Jane as the member
        driver.find_element_by_xpath('//*[@id="topDiv"]/div[1]/span/a').click()
        driver.find_element_by_id('aname').send_keys('Internal research')
        user = Select(driver.find_element_by_id('auserId_1'))
        user.select_by_visible_text('Jane Biologist')
        driver.find_element_by_css_selector('#addForm > fieldset > input[type=button]:nth-child(4)').click()

        driver.close()







