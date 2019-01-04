from selenium import webdriver
# first "pip install webdriver-manager"
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://model.arxspan.com/login.asp')
driver.maximize_window()
driver.find_element_by_id('login-email').send_keys('admin@demo.com')
driver.find_element_by_id('login-pass').send_keys('carbonCopee')
driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
select = Select(driver.find_element_by_tag_name('select'))
select.select_by_visible_text('Demo')
driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)


elms = driver.find_elements_by_tag_name('a')
for elm in elms:
    if elm.text == 'Notebooks':
        elm.click()
        links = driver.find_elements_by_tag_name('a')
        for link in links:
            if link.text.trim == ' Test_Notebook_QingWang':
                link.click()



