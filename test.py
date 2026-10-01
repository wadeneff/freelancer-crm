from database.req import getClients, initDb

print('1. Инициализировать БД\n2. Получить список клиентов')
action = int(input('Действие #:'))
if action == 1:
    initDb()
elif action == 2:
    getClients()
