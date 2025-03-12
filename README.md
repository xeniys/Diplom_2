# Diplom_2
Автотесты API учебного сервиса Stellar Burgers. 
Документация: https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89


Протестированы ручки:

Создание пользователя (/api/auth/register)
 - тесты в файле test_create_user.py

Логин пользователя (/api/auth/login)
 - тесты в файле test_user_login.py

Изменение данных пользователя (/api/auth/user)
 - тесты в файле test_edit_user_data.py

Создание заказа (/api/orders)
 - тесты в файле test_create_order.py

Получение заказов конкретного пользователя (/api/orders)
 - тесты в файле test_get_orders.py



В проекте так же есть файл с зависимостями: requirements.txt
Чтобы установить все нужные пакеты, выполнить команду

pip3 install -r requirements.txt

(Запись этой команды зависит от версии Python. 
Если у тебя третья версия, поставь тройку после pip. 
Если Python второй версии, оставь просто pip.)