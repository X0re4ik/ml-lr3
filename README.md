# Mochalov Anton

## Инструкция
В качестве s3 хранилища используется собсвтенное minio: 
* https://gitlab-tester-test.ru:8888 (UI)
* https://gitlab-tester-test.ru:8887 (console)

Пароли в файле .env.example

Какталог на момент начала выполнения pipeline-а 
```
data/
        external/
                ...
        interim/
                i_love_ml.csv <- Исходный файл
        processed/
                ...
```

Скопировать данные из .env.example в файл .env
```sh
cp .env.example .env
```
Сделать исполняемым файлы в директории scripts
```
chmod +x ./scripts/*
```

Установка зависимостей через poetry
```
poetry install
```

Выполнить скрипт pipeline-а:
```
sh ./scripts/pipeline.sh
```
По ваш каталог должен иметь следующий вид:
```
data/
        external/
                i_love_ml.csv <- Файл загруженный через S3 хранилище
        interim/
                i_love_ml.csv <- Исходный файл
        processed/
                i_love_ml.csv <- Обработанный файл из S3 хранилища
```