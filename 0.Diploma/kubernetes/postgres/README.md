Для проверки работоспособности базы данных:

1. Узнайте IP пода postgresql

kubectl get pod -o wide

2. Запустите рядом тестовый под

kubectl run -t -i --rm --image postgres:10.13 test bash

3. Внутри тестового пода выполните команду для подключения к БД

psql -h <postgresql pod IP из п.1> -U user database

Введите пароль - password

5. Проверьте что таблица создалась. Для этого все в том же тестовом поде выполните команду 

\dt