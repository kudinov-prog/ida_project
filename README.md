### Сервис для изменения размеров изображения

#### Инфраструктура
* Проект работает с БД SQLite
* Медиаданные сохраняются в папку /media

#### Стек
* Python 3.8
* Django 3.0


## Запуск проекта
Для запуска проекта клонируем данный репозиторий и переходим в корневую папку.
Создаем виртуальное окружение

```
python -m venv venv
```

Активируем его

```
source venv/scripts/activate
```

Устанавливаем необходимые зависимости из файла requirements.txt

```
pip install -r requirements.txt
```

Делаем миграции

```
python manage.py makemigrations
python manage.py migrate
```

Запускаем локально проект

```
python manage.py runserver
```

Для работы в админке нужно создать супераользователя и зайти под ним

```
python manage.py createsuperuser
```

Если всё сделано правильно, то проект будет доступен по адресу

```
http://127.0.0.1:8000/
```
