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


class TestCreatedropdownsAdmin(unittest.TestCase):

    @allure.testcase('test_create_dropdowns_by_admin')
    def test_create_dropdowns_by_admin(self):
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

        # Create new dropdowns
        driver.find_element_by_xpath('//*[@id="navOrders"]/li[4]/a').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_class_name('editorFieldInput').send_keys('Q_Testing_Dropdowns')
        option = driver.find_element_by_xpath('//*[@id="reactDropdownEditor"]/div/div[4]/div/div[1]/button')
        actions = ActionChains(driver)
        actions.double_click(option).perform()
        driver.find_elements_by_class_name('optionDisplayName')[0].send_keys('Apple')
        driver.find_elements_by_class_name('optionDisplayName')[1].send_keys('Banana')
        driver.find_elements_by_class_name('optionDisplayName')[2].send_keys('Carrot')
        driver.find_element_by_css_selector('#reactDropdownEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Edit the masking value of dropdowns
        driver.find_elements_by_class_name('sorting_1')[0].click()
        # driver.execute_script("arguments[0].click();", dropdown)
        driver.find_element_by_id('dropdownEditor_maskValues_cb').click()
        driver.find_element_by_css_selector(
            '#dropdownOptionsTable > tbody > tr:nth-child(1) > td:nth-child(3) > button').click()
        driver.find_elements_by_class_name('maskValueInput')[0].clear()
        driver.find_elements_by_class_name('maskValueInput')[0].send_keys('Ca')
        driver.find_element_by_css_selector(
            '#dropdownOptionsTable > tbody > tr:nth-child(2) > td:nth-child(3) > button').click()
        driver.find_elements_by_class_name('maskValueInput')[0].clear()
        driver.find_elements_by_class_name('maskValueInput')[0].send_keys('Ba')
        driver.find_element_by_css_selector(
            '#dropdownOptionsTable > tbody > tr:nth-child(3) > td:nth-child(3) > button').click()
        driver.find_elements_by_class_name('maskValueInput')[0].clear()
        driver.find_elements_by_class_name('maskValueInput')[0].send_keys('Ap')
        driver.find_element_by_css_selector('#reactDropdownEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create another dropdown
        driver.find_element_by_xpath('//*[@id="navOrders"]/li[4]/a').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_class_name('editorFieldInput').send_keys('Q_Testing_Dropdowns2')
        driver.find_element_by_xpath('//*[@id="reactDropdownEditor"]/div/div[4]/div/div[1]/button').click()
        driver.find_elements_by_class_name('optionDisplayName')[0].send_keys('Yes')
        driver.find_elements_by_class_name('optionDisplayName')[1].send_keys('No')
        driver.find_element_by_css_selector('#reactDropdownEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        driver.close()

