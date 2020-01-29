from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")
x_element = driver.find_element_by_css_selector("#num1")
x = int(x_element.text)
x_element = driver.find_element_by_css_selector("#num2")
y = int(x_element.text)
x=x+y
select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(str(x))
option1 = driver.find_element_by_css_selector("[type=submit]")
option1.click()