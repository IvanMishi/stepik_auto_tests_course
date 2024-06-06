# Поиск элемента в выпадающем списке с помощью метода select_by_value() из библиотеки Selenium

## Инженер по тестированию переходит в директорию, предназначенную для хранения файлов с тестами
```
cd selenium_tests
```
## Из директории selenium_tests активирует виртуальное окружение
```sh
source selenium_env/bin/activate
```
## В активированном окружении запускает тест 
```sh
python3 TEST8/TEST8.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 TEST8/TEST8.py >> TEST8/output.txt
```
Где TEST7.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.

## Тестовые данные
- Незарегестированный пользователь переходит по ссылке https://suninjuly.github.io/selects1.html
- Находит и получает текст из элементов с числами на этой странице
- Складывает значения элементов и сохраняет результат в переменную
- Выбирает в выпадающем списке элемент, значение которого равно сумме чисел
- Нажимает на кнопку "Submit"
- Закрывает браузер

##  В этой задаче

Программа ищет элемент c помощью метода select_by_value() из библиотеки Selenium WebDriver который используется для работы с выпадающими списками (dropdown) на веб-странице. \
Когда на веб-странице есть элемент <select> (выпадающий список) с дочерними элементами <option>, у каждого из которых есть атрибут value, \
метод select_by_value() позволяет выбрать опцию из выпадающего списка, основываясь на значении value атрибута элемента <option>.