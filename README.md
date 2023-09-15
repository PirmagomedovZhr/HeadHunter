Data Service API

Это простое Django-приложение, которое предоставляет HTTP API для загрузки CSV-файлов, получения списка файлов и извлечения данных из них.

Установка и запуск:

    Запустите виртуальное окружение:
        source env/bin/activate

    Установите зависимости:
        pip install -r requirements.txt

    Примените миграции:
        cd service
        python manage.py makemigrations
        python manage.py migrate

    Запустите сервер Django:
        python manage.py runserver


По умолчанию, сервер будет запущен на http://localhost:8000/.


API Endpoint
Загрузка файла

    URL: /api/uploaded-files/

    Метод: POST

    Описание: Загрузка файла в формате CSV.

    Параметры запроса: Файл с данными.

    Пример запроса c использованием curl:
        curl -X POST -F "file=@/путь/к/вашему/файлу.csv" http://localhost:8000/api/uploaded-files/


Получение списка файлов

    URL: /api/uploaded-files/

    Метод: GET

    Описание: Получение списка загруженных файлов с информацией о колонках.

    Пример запроса с использованием curl:
        curl http://localhost:8000/api/uploaded-files/


Получение данных из файла

    URL: /api/uploaded-files/{file_id}/get-data/

    Метод: GET

    Описание: Получение данных из конкретного файла с опциональной фильтрацией и сортировкой.

    Параметры запроса: Фильтры и параметры сортировки (если необходимо).

    Пример запроса с использованием curl:
        curl http://localhost:8000/api/uploaded-files/{file_id}/get-data/
