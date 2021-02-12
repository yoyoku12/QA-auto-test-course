from selenium import webdriver
import math
import time


#Открываем страницу
driver = webdriver.Chrome()
driver.get("http://SunInJuly.github.io/execute_script.html") 
#Считаем значение для переменной x
x = driver.find_element_by_xpath('//*[@id="input_value"]').text
#Вычесляем значение функции
y = math.log(abs(12*math.sin(int(x))))

y = str(y)

driver.execute_script("window.scrollBy(0, 100);")
driver.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

time.sleep(2)

driver.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
driver.find_element_by_xpath('//*[@id="robotsRule"]').click()
driver.find_element_by_xpath('/html/body/div/form/button').click()

time.sleep(5)

driver.quit()

