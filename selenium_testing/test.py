from selenium import webdriver
# first "pip install webdriver-manager"
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000')
driver.find_element_by_id('demo').click()

