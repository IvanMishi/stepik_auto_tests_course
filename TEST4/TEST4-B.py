# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

# ссылка на страницу 
link = "http://suninjuly.github.io/huge_form.html"

# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае.
try:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

    
# Каскадный поиск:  находит родительский элемент, затем находит дочерние элементы внутри родительского, которые являются элементами ввода (input) c помощью метода find_elements()

# ищет родительский элемент
    parent_element = browser.find_element(By.CSS_SELECTOR, 'form[action="#"][method="get"]')

# проходит по каждому дочернему элемемену внутри родительского с тегом 'input' и вводит текст "Мой ответ"
    [child_element.send_keys("Мой ответ") for child_element in parent_element.find_elements(By.TAG_NAME, "input")]        


# находит и нажимает кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

# код внутри блока finally будет выполнен в любом случае
finally:
    # успевает скопировать код за 10 секунд
    time.sleep(10)
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла