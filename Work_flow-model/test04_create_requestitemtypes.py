import time, re, os
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > div:nth-child(2) > div.card-header '
                                            '> div > button').click()
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > '
                                            'div.dropdownEditorContainer.requestItemTypesPage.card.makeVisible > '
                                            'div:nth-child(1) > input').send_keys('Q_Testing_requestitemtypes')
        restrictaccess = driver.find_element_by_name('dropdownEditor_restrictAccess_cb')
        restrictaccess.click()

        # Add CRO one group can view, can edit, can be assigned
        driver.find_element_by_xpath('//*[@id="requestTypeAllowedGroupsEditorSection"]/div/div[1]/button[1]').click()
        driver.find_element_by_id('CRO oneCanView').click()
        driver.find_element_by_id('CRO oneCanEdit').click()
        driver.find_element_by_id('CRO oneCanBeAssigned').click()

        # Add Internal research group can add, can view, can edit
        driver.find_element_by_xpath('//*[@id="requestTypeAllowedGroupsEditorSection"]/div/div[1]/button[2]').click()
        driver.find_element_by_id('Internal researchCanAdd').click()
        driver.find_element_by_id('Internal researchCanView').click()
        driver.find_element_by_id('Internal researchCanEdit').click()

        # Add Workflow manager group can add, can view, can edit
        driver.find_element_by_xpath('//*[@id="requestTypeAllowedGroupsEditorSection"]/div/div[1]/button[3]').click()
        driver.find_element_by_id('Wrokflow managerCanAdd').click()
        driver.find_element_by_id('Wrokflow managerCanView').click()
        driver.find_element_by_id('Wrokflow managerCanEdit').click()
        driver.find_element_by_id('Wrokflow managerCanDelete').click()

        # Add four fields
        driver.find_element_by_css_selector('#requestTypeFieldsEditorSection > div > div.aboveEditorItemContainer > '
                                            'div.aboveEditorTableButtonsContainer > button').send_keys(Keys.TAB)
        driver.find_element_by_css_selector('#requestTypeFieldsEditorSection > div > div.aboveEditorItemContainer > '
                                            'div.aboveEditorTableButtonsContainer > button').click()
        # ActionChains(driver).click(driver.find_element(By.CLASS_NAME, 'savedFieldDropdown')).perform()
        field1 = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr > '
                                                            'td.savedFieldDropdownTD > select'))
        field1.select_by_visible_text('Q_Testing_Fields_Structure')
        driver.find_element_by_css_selector('#requestTypeFieldsEditorSection > div > div.aboveEditorItemContainer > '
                                            'div.aboveEditorTableButtonsContainer > button').click()
        field2 = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(2) > '
                                                            'td.savedFieldDropdownTD > select'))
        field2.select_by_visible_text('Q_Testing_Fields_DropDown')
        driver.find_element_by_css_selector('#requestTypeFieldsEditorSection > div > div.aboveEditorItemContainer > '
                                            'div.aboveEditorTableButtonsContainer > button').click()
        field3 = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(3) > '
                                                            'td.savedFieldDropdownTD > select'))
        field3.select_by_visible_text('Q_Testing_Fields_FileAttachment')
        driver.find_element_by_css_selector('#requestTypeFieldsEditorSection > div > div.aboveEditorItemContainer > '
                                            'div.aboveEditorTableButtonsContainer > button').click()
        field4 = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(4) > '
                                                            'td.savedFieldDropdownTD > select'))
        field4.select_by_visible_text('Q_Testing_Fields_Registration')
        driver.find_element_by_css_selector('#arxWorkflowContainer > div > div > '
                                            'div.dropdownEditorContainer.requestItemTypesPage.card.makeVisible > '
                                            'div.bottomButtons > '
                                            'button.dropdownEditorSubmit.submitButton.btn.btn-success').click()

        # Edit fields "structure", select " Clear when duplicated" and updated
        driver.find_element_by_xpath('// *[ @ id = "dropdownsTable"] / tbody / tr / td[3]').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsTable"]/tbody/tr[1]/td[5]/button').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div[6]/input').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div[14]/button[1]').click()
        driver.find_element_by_xpath('//*[@id="arxWorkflowContainer"]/div/div/div[1]/div[20]/button[1]').click()

        # Edit fields "dropdown", select "banana" as the default value and updated
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsTable"]/tbody/tr[2]/td[5]/button')
        defaultvalue = Select(driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div['
                                                           '12]/select'))
        defaultvalue.select_by_visible_text('Banana')
        driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div[14]/button[1]').click()

        # Create new request item type
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[4]/a/span[2]').click()
        driver.find_element_by_xpath('//*[@id="arxWorkflowContainer"]/div/div/div[2]/div[1]/div/button').click()
        driver.find_element_by_class_name('editorFieldInput').send_keys('Qing_testing02')

        driver.find_element_by_xpath('//*[@id="requestTypeFieldsEditorSection"]/div/div[1]/div[1]/button').click()
        textfield = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(1) > '
                                                               'td.savedFieldDropdownTD > select'))

        textfield.select_by_visible_text('Q_Testing_Fields_Text')
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsEditorSection"]/div/div[1]/div[1]/button').click()
        textfield2 = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(2) > '
                                                                'td.savedFieldDropdownTD > select'))
        textfield2.select_by_visible_text('Q_Testing_Fields_Text')
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsEditorSection"]/div/div[1]/div[1]/button').click()
        dropdownfield = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(3) '
                                                                   '> td.savedFieldDropdownTD > select'))
        dropdownfield.select_by_visible_text('Q_Testing_Fields_DropDown')
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsEditorSection"]/div/div[1]/div[1]/button').click()
        authorfield = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(4) > '
                                                                 'td.savedFieldDropdownTD > select'))
        authorfield.select_by_visible_text('Q_Testing_Fields_CoAuthors')
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsEditorSection"]/div/div[1]/div[1]/button').click()
        longtextfield = Select(driver.find_element_by_css_selector('#requestTypeFieldsTable > tbody > tr:nth-child(5) '
                                                                   '> td.savedFieldDropdownTD > select'))
        longtextfield.select_by_visible_text('Q_Testing_Fields_LongText')
        driver.find_element_by_xpath('//*[@id="arxWorkflowContainer"]/div/div/div[1]/div[20]/button[1]').click()

        # Edit fields "text", select "Required" checkbox and updated
        driver.find_element_by_xpath('//*[@id="workflowAdminNavMenu"]/li/div/ul/li[4]/a/span[2]').click()
        driver.find_element_by_xpath('//*[@id="dropdownsTable"]/tbody/tr[2]/td[1]').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsTable"]/tbody/tr[1]/td[5]/button').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div[2]/input').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div[14]/button[1]').click()

        # Edit fields "co-author", select "Allow multiple value" checkbox and updated
        driver.find_element_by_xpath('//*[@id="requestTypeFieldsTable"]/tbody/tr[4]/td[5]/button').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div[3]/input').click()
        driver.find_element_by_xpath('//*[@id="requestTypeFieldEditorModal"]/div/div/div/div[14]/button[1]').click()

        driver.find_element_by_xpath('//*[@id="arxWorkflowContainer"]/div/div/div[1]/div[20]/button[1]').click()
        driver.close()
