from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element_by_css_selector("#input_value")
x = int(x_element.text)
x = calc(x)
browser.execute_script("window.scrollTo(0,document.scrollingElement.scrollHeight);")
option1 = browser.find_element_by_css_selector("[value='robots']")
option1.click()
option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option1 = browser.find_element_by_id("answer").send_keys(x)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()