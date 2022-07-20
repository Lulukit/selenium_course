from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def sum(x, y):
    return str(x + y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который считает сумму чисел и записывает в переменную
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_element.text)
    sum_elem = sum(x, y)

    # Ищем элемент с текстом равным сумме чисел
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_visible_text(sum_elem) 

    # Жмем на кнопку сабмит

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
