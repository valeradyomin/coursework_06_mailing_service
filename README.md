# Сервис управления рассылками, администрирования и получения статистики.

_Дополнительно реализован раздел блога._

Шаги для установки сервиса

Клонировать проект

Установить зависимости в venv

    pip install -r requirements.txt

* Создать базу данных для проекта в СУБД postgres
* В файл .env внести и/или изменить данные настроек конфигурации проекта (референс .env.sample)
* Для того, чтобы работало кэширование, необходимо установить redis

Выполнить команды, чтобы создать таблицы и связи в базе данных

    python manage.py makemigrations     
    python manage.py migrate



Выполнить команду для создания суперпользователя

    python manage.py create_su

При регистрации пользователя, ему необходимо активировать почту.
Письмо с подтверждением отправляется на контактный email.



В административной панели или через консоль добавить группу менеджера и задать полномочия.

Функционал менеджера

    + Может просматривать любые рассылки
    + Может просматривать список пользователей сервиса
    + Может блокировать пользователей сервиса
    + Может отключать рассылки
    + Может создавать, изменять и удалять записи блога
    - Не может редактировать рассылки
    - Не может управлять списком рассылок
    - Не может изменять рассылки и сообщения

При необходимости выполнить команду для заполнения базы данных тестовыми данными

    python manage.py loaddata data.json

Запустить сайт

    python manage.py runserver

По ссылке в терминале отобразится содержимое сайта

Для старта выполнения периодических рассылок ввести команду
    
    python manage.py runapscheduler


