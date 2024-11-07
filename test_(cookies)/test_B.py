import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
import json # Модуль для преобразования в формат json
from selenium.webdriver.common.by import By
import re

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.6/1/index.html'
# Измеряет время выполнения.
start = time.time()

# Чтение куков из текстового файла
with open('cookie_dict.txt', 'r') as file:  # Открывает текстовый файл для чтения
    cookie_dict = json.load(file)  # Читает и загружает куки как список словарей

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Пустой список для хранения результатов
    result = []
    # Добавляет все куки из словаря
    for cookie in cookie_dict:
        webdriver.add_cookie(cookie)
        webdriver.refresh()

        # Получаем значение куки у каждого кандидата
        for skill in webdriver.get_cookies():
            val_cookie = skill['value']  # Берем последнее значение куки

        # Получает возраст в числовом знаении
        age = webdriver.find_element(By.ID, "age").text
        # Проверка наличия цифр в строке age
        match = re.search(r'\d+', age)
        if match:
            age_value = int(match.group())
        else:
            print(f'Возраст не найден или имеет неверный формат у кандидата с значением куки:.{val_cookie}')

        # Получаем список навыков
        skill_list = webdriver.find_elements(By.CSS_SELECTOR, "#skillsList > li")
        # Получение количества навыков
        num_skills = len(skill_list)
        # Добавляем результаты в список как кортеж
        result.append((age_value, num_skills, val_cookie))
        # Удаляем все куки перед следующим циклом
        webdriver.delete_all_cookies()
        # Печатаем данные о кандидатах для отладки
        print(f'Возраст:{age_value} Количество навыков: {num_skills} Значение куки: {val_cookie}')

candidat_find = max(result, key=lambda x: (-x[0], x[1]))
print(f'Самый молодой кандидат имеет возраст: {candidat_find[0]} и наиболшее количество навыков в возрастной категории: {candidat_find[1]} Значение его куки: {candidat_find[2]}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`