from selenium import webdriver
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
option1 = browser.find_element_by_css_selector("[name='firstname']")
option1.send_keys("Denis")
option1 = browser.find_element_by_css_selector("[name='lastname']")
option1.send_keys("Chernikov")
option1 = browser.find_element_by_css_selector("[name='email']")
option1.send_keys("Deniskachernikov@ya.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
option1 = browser.find_element_by_css_selector("#file")
print(file_path)
option1.send_keys(file_path)
button = browser.find_element_by_tag_name("button")
button.click()