<<<<<<< HEAD
# tortured-phrase-spotter
=======
# Tortured Phrase Spotter

Инструмент для поиска и выделения "трудных" фраз в тексте с рекомендациями по их замене.

## Установка

1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```
   pip install openpyxl
   ```

## Запуск

1. Поместите текст для анализа в файл `sample.txt` (UTF-8).
2. Убедитесь, что файл фраз и рекомендаций называется `🤷_tortured.csv` и находится в корне проекта.
3. Запустите инструмент:
   ```
   python3 src/run_spotter.py
   ```
4. Результаты появятся в консоли, а также в файлах `report.html` и `report.txt`.

## Структура проекта

- `src/` — исходный код
- `🤷_tortured.csv` — CSV-файл с фразами для поиска и рекомендациями (1-й столбец — искать, 2-й — рекомендовать)
- `sample.txt` — текст для анализа
- `report.html` — HTML-отчёт с выделением найденных фраз и рекомендациями
- `report.txt` — текстовый отчёт с результатами

## Редактирование списка фраз

1. Откройте файл `🤷_tortured.csv` в редакторе таблиц (Excel, Numbers, LibreOffice и др.).
2. В первый столбец вносите фразы, которые нужно искать в тексте.
3. Во второй столбец — рекомендации по замене.
4. Сохраните файл в формате CSV (UTF-8).

## Пример содержимого 🤷_tortured.csv

```
"Fingerprint - Tortured Phrase","Expected Text"
"tortured phrase","simple phrase"
"complex expression","simple expression"
```

## Пример sample.txt

```
This is a tortured phrase. Here is a complex expression.
```

## Пример отчёта

- `report.html` — откройте в браузере для просмотра выделенных фраз и рекомендаций.
- `report.txt` — текстовый вариант отчёта для быстрой проверки. 
>>>>>>> a43d72c (Initial commit)
