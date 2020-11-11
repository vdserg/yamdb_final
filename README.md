# API для сервиса YAMDB
#### Проект выполнялся в рамках учебного курса [Яндекс.Практикум](https://praktikum.yandex.ru/backend-developer/)
## Установка
#### 1. Установка docker и docker-compose
Инструкция по установке доступна в официальной [инструкции](https://www.docker.com/get-started)

#### 2. Создать файл .env с переменными окружения
````
POSTGRES_DB=yamdb #Название базы данных
POSTGRES_USER=postgres # Администратор базы данных
POSTGRES_PASSWORD=postgres # Пароль администратора
DB_HOST=db
DB_PORT=5432
NGINX_PORT=80
NGINX_SERVER_NAME=localhost #Адрес сервера
````

#### 3. Сборка и запуск контейнера
````bash
docker-compose up -d --build
````
#### 4. Сбор статики
````bash
docker-compose exec web python manage.py collectstatic --noinput
````
#### 5. Создание суперпользователя Django
````bash
docker-compose exec web python manage.py createsuperuser
````
#### 6. Инициализация тестовых данных:
````bash
docker-compose exec web python manage.py loaddata fixtures.json
````

### Работа с api
Документация доступна в redoc

## Основные использованные технологии
* [python 3.8](https://www.python.org)
* [django](https://www.djangoproject.com/)
* [django rest framework](https://www.django-rest-framework.org/)
* [PostreSQL](https://postgresql.com/)
* [docker](https://www.docker.com)
