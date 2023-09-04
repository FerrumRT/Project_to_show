1. Чтобы скачать с гитхаба проект и запустить, делаем следующие шаги:

    1. Создаем пустую папку на рабочем столе(можно в других местах) и задаем любое имя.

    2. Открываем командную строку. Через командную строку переходим в ту папку который создали или заходим в эту папку, и на верху будет путь к этой папке,

    ![image](https://user-images.githubusercontent.com/57407430/122340904-af520780-cf64-11eb-9e29-ac6abf0d358d.png)

    нажимаем на это место 

    ![image](https://user-images.githubusercontent.com/57407430/122341166-fdffa180-cf64-11eb-8c94-a45463d55603.png)

    и пишем cmd.

    ![image](https://user-images.githubusercontent.com/57407430/122341297-24bdd800-cf65-11eb-8c5c-8bbd08054556.png)

    3. После выполнения 1.2 пункта, в командной строке пишем `git clone https://github.com/FerrumRT/Project_to_show.git`

2. Запуск проекта

    1. Заходим в папку Project_to_show через коммандную строку и запускаем комманду `python -m venv venv` для создания виртуального окружения

    3. Заходим в виртуальное окружение с помощью комманды
       
        1. на Windows `venv\Scripts\activate`
           
        3. на Linux и MacOS `source venv/bin/activate`
           
    5. Для установки нужных библиотек пишем `pip install -r requirements.txt`
       
    7. Заходим в папку project через коммандную строку и пишем `python manage.py migrate` для миграции базы данных в виде файла db.sqlite3
       
    9. Для непосредственно запуска проекта локально нужно запустить комманду `python manage.py runserver` и открыть в браузере [localhost:8000](http://localhost:8000)
