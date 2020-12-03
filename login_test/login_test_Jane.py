#!/usr/bin/python
# -*- coding: utf-8 -*-
# Test ID: test-01
# Test name: Login Test
# Expect output: Login successful
# Step description:
#      1. Open the Chrome driver;
#      2. Launch the URL of login page;
#      3. Input the Joe as the username;
#      4. Input the password;
#      5. Choose the different company;
#      6. Successfully login
from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import platform
import unittest, time, re, os


class TestWitnessJane(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(executable_path=IEDriverManager().install())
        # chrome_options = Options()
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--disable-gpu')
        # if platform.system() == 'Windows':
        #     self.driver = webdriver.microsoft(IEDriverManager().install(), chrome_options=chrome_options)
        # elif platform.system() == "Darwin":
        #     self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
        # else:
        #     self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
        #
        self.driver.implicitly_wait(20)
        self.base_url = "https://eln.arxspan.com/login.asp?action=&override=hmwc"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_reject_chemistrywitness_jane(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('BobRossPositiveEnergy')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Workflow Demo Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)

        # select the chemistry experiment in witness request list
        button = driver.find_element_by_xpath('//*[@id="witnessRequestHolder"]/DIV/DIV[2]/TABLE/TBODY/TR[1]/TD[2]/A')
        button.click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "#witnessButtons > a:nth-child(2)"))).click()
        time.sleep(2)

        # add a note to reject reason
        driver.find_element_by_id('reasonBox').send_keys('TESTING')
        # reject the witness request
        driver.find_element_by_id('rejectSubmitButton').click()
        time.sleep(6)

        driver.find_element_by_link_text('Logout').click()
        time.sleep(2)
        driver.close()
