# Jushma_Test

Привет - привет

Инструкция:
 1. Клонировать репозиторий: git clone https://github.com/aSel1x/Jushma_Test
 2. Запустить: docker-compose up -d или uvicorn app:app --host 127.0.0.1 --port 8000
 3. Применить миграции: litestar database upgrade
 4. Сколько ушло времени на реализацию: часов 6
    > Самым сложным оказалось выяснить то, то cli litestar по имени 'database' не работал, тк папка приложения называлась не app, а src.
    
    > Старался сделать максимально по ТЗ