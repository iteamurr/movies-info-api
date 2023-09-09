# Данные

Данные взяты из [Сведения о показах фильмов в кинозалах](https://opendata.mkrf.ru/opendata/7705851331-movie_gross).

В проекте оставлен флаг `DEBUG = True`, чтобы можно было потыкать в DRF кнопки в `http://0.0.0.0:8080/api/`. В меню `Filters` в правом верхнем углу можно задать поле, по которому будет идти сортировка, и поисковый запрос.

# Проект

В приложении api в файле [importdata.py](src/api/management/commands/importdata.py) написан парсер .csv файла, который переносит данные в базу данных. Реализовал ее в виде утилиты, которую можно запускать командой:

```
python manage.py importdata <.csv файл с данными>
```

# Ручки

Детальную информацию по API можно посмотреть в [openapi-schema.yml](openapi-schema.yml).

`http://0.0.0.0:8080/api/` — Возвращает список фильмов по 25 элементов на странице. Этот список можно сортировать по каждому полю фильма. Также встроен поиск, который идет по полям `name` и `distribution_id`.

`http://0.0.0.0:8080/api/<movie_id:uuid>` — Возвращает информацию по конкретному фильму. Поиск идет по `movie_id`.

# Развертывание

## Для разработки

1. Создать `.env` файл:
```
make env
```
2. Запустить базу данных:
```
make db
```
3. Установить зависимости и запустить виртуальную оболочку:
```
poetry install
poetry shell
```
4. Применить миграции и заполнить базу данных:
```
make migrate
make importdata
```
5. Запустить проект:
```
make run
```

## В контейнере


