# Скрипты для правки электронного дневника хакера Вани
[for e-diary devman project](https://github.com/devmanorg/e-diary/tree/master)

## Техническое описание
Три скрипта помогающие хакеру Ване представить своей маме ситуацию с учебой в ином свете, и доказывающие приемущество програмиста перед будующим юристом.

 - fix_marks(schoolkid) - принимает имя ученика(вдруг друзья попросят). Добавляет 2 к  оценкам 3 и ниже
 - remove_chastisements(schoolkid) - принимает имя ученика. Удаляет все замечания данного ученика
 - create_commendation(name, subject) - принимает имя ученика и предмет. Генерирует в дневник случайную похвалу ученику от учителя соответствующего предмета. Время будет установлено последнего прошедшего предмета.

## Системные требования
[Python 3](https://www.python.org/)

##  Установка
Для установки дастоточно:

Cклонировать проект

       git clone https://github.com/toshiharu13/hack_school_db-joke-.git

Скопировать файл script.py в корень заранее развернутого проекта 

[e-diary](https://github.com/devmanorg/e-diary.git)
 
Открыть терминал в дериктории проекта и ввести

      python manage.py shell
В Django shell импортировать функции скопированного файла

      from scripts import fix_marks, remove_chastisements, create_commendation
## Запуск

в Django shell ввести имя функции с параметрами, пример:

      fix_marks('<Имя ученика>')