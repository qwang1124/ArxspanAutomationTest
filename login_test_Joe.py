#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

usr = 'joe@demo.com'
pwd = 'carbonCopee'


class TestLoginPage(unittest.TestCase):

	# Test successful login with Joe select different option of company

	def testSuccessfulLogin1(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')
		# Open the login page

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		# Sign in the username

		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		# Sign in the password

		elem.send_keys(Keys.RETURN)
		# Click to sign in

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('Demo')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		self.assertEqual('foo'.upper(), 'FOO')
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')

	def testSuccessfulLogin2(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')
		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('Accent Tx Model')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')

	def testSuccessfulLogin3(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')
		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('Apollo')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Demo')

	def testSuccessfulLogin4(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')
		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('BIM')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Demo')

	def testSuccessfulLogin5(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')
		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('CpdTrackingNoInv')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')

	def testSuccessfulLogin6(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('CT DEMO')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')

	def testSuccessfulLogin7(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('Formulation Demo')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')

	def testSuccessfulLogin8(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('Model Test Script Company')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')

	def testSuccessfulLogin9(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('Relay Test')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joey Chemical')

	def testSuccessfulLogin10(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('S Multi Author')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')

	def testSuccessfulLogin10(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('VBU Model')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'joe demo')

	def testSuccessfulLogin11(self):
		driver = webdriver.Chrome("C:\\Users\\Ms. Wang\\PycharmProjects\\myfirst\\driver\\chromedriver.exe")
		driver.get('https://model.arxspan.com/login.asp')

		elem = driver.find_element_by_id('login-email')
		elem.send_keys(usr)
		elem = driver.find_element_by_id('login-pass')
		elem.send_keys(pwd)
		elem.send_keys(Keys.RETURN)

		select = Select(driver.find_element_by_tag_name('select'))
		select.select_by_visible_text('Workflow Pilot - ARV')
		elem = driver.find_element_by_id('login-submit')
		elem.send_keys(Keys.ENTER)
		name = driver.find_elements_by_class_name('headUserName')[0].text
		self.assertEqual(name, 'Joe Chemist')


if __name__ == '__main__':
	unittest.main()