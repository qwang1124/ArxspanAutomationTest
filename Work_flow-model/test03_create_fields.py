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


class TestCreatefieldsAdmin(unittest.TestCase):

    @allure.testcase('test_create_fields_by_admin')
    def test_create_fields_by_admin(self):
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

        # Create new Drop Down field
        driver.find_element_by_xpath('//*[@id="navOrders"]/li[5]/a').click()
        # # driver.find_element_by_class_name('sidebar-normal').click()
        # driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
        #                                     'div > button').click()
        # driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
        #     'Q_Testing_Fields_DropDown')
        # driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(2) > div > input').send_keys('F&V')
        # datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
        #                                                       'select'))
        # datatype.select_by_visible_text('Drop Down')
        # customdropdown = Select(driver.find_element_by_id('savedDropdownsListDropdown'))
        # customdropdown.select_by_visible_text('Q_Testing_Dropdowns')
        # checkbox = driver.find_element_by_id('savedDropdownsListSyncCheckbox')
        # checkbox.click()
        # driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
        #                                     'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Text field
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Text')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Text')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Long Text fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_LongText')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Long Text')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Integer fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Integer')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Integer')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Real Number fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_RealNumber')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Real Number')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create File Attachment fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_FileAttachment')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('File Attachment')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Date fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Date')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Date')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Structure fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Structure')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Structure')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(6) > div > input').send_keys('400')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(7) > div > input').send_keys('300')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Rich Text fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_RichText')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Rich Text')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create User List fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_User List')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('User List')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Co-Authors fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_CoAuthors')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Co-Authors')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Notebook fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Notebook')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Notebook')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Project fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Project')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Project')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Experiment fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Experiment')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Experiment')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Registration fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Registration')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Registration')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Request fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_Request')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Request')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Create Foreign Link fields
        driver.refresh()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[2]/a/span[2]').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(3) > div.card-header > '
                                            'div > button').click()
        driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(1) > div > input').send_keys(
            'Q_Testing_Fields_ForeignLink')
        datatype = Select(driver.find_element_by_css_selector('#reactFieldEditor > div > div:nth-child(3) > div > '
                                                              'select'))
        datatype.select_by_visible_text('Foreign Link')
        driver.find_element_by_css_selector('#reactFieldEditor > div > div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        driver.close()
