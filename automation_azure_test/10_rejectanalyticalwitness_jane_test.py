# Test ID: testELN-011
# Test name: Jane has reject the analytical experiment witness request by Joe Test
# Expect output:
#      1. Check received witness request from Joe is showing ;
#      2. Add a new note;
#      3. Successful reject witness request send by Joe;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Check the witness request is showing the notification;
#      5. Select the analytical experiment name which shared by Joe;
#      6. Add a new note;
#      7. Reject the witness request
#      8. Log out.
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import platform
import json


class TestWitnessJane(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        if platform.system() == 'Windows':
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        elif platform.system() == "Darwin":
            self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

        self.driver.implicitly_wait(3)
        self.base_url = "https://model.arxspan.com/login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_reject_analyticalwitness_jane(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.implicitly_wait(20)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        # check the witness requests is showing the notification
        assert driver.find_element_by_id('witnessRequestsHolder').is_displayed()
        # select the analytical experiment name
        driver.find_element_by_xpath('//*[@id="witnessRequestsHolder"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "#witnessButtons > a:nth-child(2)"))).click()
        # add a note to reject reason
        driver.find_element_by_id('reasonBox').send_keys('TESTING')
        # reject the witness request
        driver.find_element_by_id('rejectSubmitButton').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        driver.find_element_by_link_text('Logout').click()
        driver.close()



