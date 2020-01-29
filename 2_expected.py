from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100")
    )
browser.find_element_by_css_selector("#book").click()    
x_element = browser.find_element_by_css_selector("#input_value")
x = int(x_element.text)
x = calc(x)
option1 = browser.find_element_by_css_selector(".form-control")
option1.send_keys(x)
option1 = browser.find_element_by_css_selector("[type=submit]")
option1.click()
