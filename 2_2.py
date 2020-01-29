import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/math.html")
x_element = driver.find_element_by_css_selector("#input_value")
x = int(x_element.text)
y = calc(x)
option1 = driver.find_element_by_css_selector("[value='robots']")
option1.click()
option1 = driver.find_element_by_css_selector("#robotCheckbox")
option1.click()
option1 = driver.find_element_by_id("answer").send_keys(y)
option1 = driver.find_element_by_css_selector("[type=submit]")
option1.click()
