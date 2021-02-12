from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
driver.find_element_by_xpath('//*[@id="book"]').click()

x = driver.find_element_by_xpath('//*[@id="input_value"]').text
x = int(x)

y = str(math.log(abs(12*math.sin(x))))

driver.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

driver.find_element_by_xpath('//*[@id="solve"]').click()
