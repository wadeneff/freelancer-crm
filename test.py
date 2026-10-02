from database.req import addClient, getClients, initDb

print('1. Инициализировать БД\n2. Получить список клиентов\n3. Пользователь test')
action = int(input('Действие #:'))
if action == 1:
    initDb()
elif action == 2:
    getClients()
elif action == 3:
    addClient('test', 'test', 'test')
