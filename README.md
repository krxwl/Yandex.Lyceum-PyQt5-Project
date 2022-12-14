# Библиотека программиста

Легкая в использовании библиотека книг с минималистичным дизайном.

## Установка
    git clone https://github.com/krxwl/Yandex.Lyceum-PyQt5-Project.git
    pip install -r requirements.txt

# Использование
    python main.py

# Описание работы программы
При запуске приложения вы можете видеть, что у него имеется несколько вкладок: “Главная”, “Библиотека” и “Жанры”.
</br></br>Во вкладке “Главная” находятся подборки книг с их обложками по различной тематике. При нажатии на обложку одной из книг появляется окно с краткой информацией о книге (а именно: ID, название, автор, обложка и год издания)  и с кнопкой, при нажатии на которую Вас перенаправляют в мессенджер Telegram, где хранится файл книги.
</br></br>Во вкладке “Библиотека” находятся: база данных, представленная в табличном виде; несколько кнопок “Редактировать элемент”, “Добавить элемент” и “Удалить элемент”. Для того чтобы редактировать табличный элемент, вы должны нажать на существующий элемент, а затем на кнопку “Редактировать элемент”. Чтобы удалить элемент, вы должны нажать на существующий элемент, а затем на кнопку “Удалить элемент”. Также присутствует возможность сортировки табличных элементов.</br></br>Во вкладке “Жанры” находятся жанры существующих книг, представленные в табличном виде. Присутствует возможность сортировки элементов и их получения в жанре txt. Для того чтобы узнать информацию о книге нужно нажать на табличный элемент во вкладке  “Библиотека”.
# Таблицы Баз Данных 
Как уже упоминалось в пункте “Описание работы программы”, во вкладке “Библиотека” содержится таблица, представляющая из себя базу данных книг. Она состоит из полей: идентификатор (id), название, автор, жанр, год и ссылки на скачивание. Во вкладке “Жанр” содержится таблица, представляющая из себя базу данных жанров. Она состоит из полей: идентификатор (id) и жанр.
# Необходимые библиотеки 
### PyQt 5 
### sqlite3 
### webbrowser 
### sys
