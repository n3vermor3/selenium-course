from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element_by_css_selector("#input_value")
x = int(x_element.text)
x = calc(x)
option1 = browser.find_element_by_css_selector(".form-control")
option1.send_keys(x)
option1 = browser.find_element_by_css_selector("[type=submit]")
option1.click()