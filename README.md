Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:yandex-praktikum/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver
Нижний колонтитул
© 2022 GitHub, Inc.
Навигация по нижнему колонтитулу
Условия
Конфиденциальность
Безопасность
Описание:
Социальная сеть. Предназначен для интресных статей писателей и тех кто хочет показать миру свою статью
Любая тема в том числе и научные и бытовые темы
Примеры запросов:
http://127.0.0.1:8000/api/v1/posts/
http://127.0.0.1:8000/api/v1/posts/{id}/
