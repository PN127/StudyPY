contacts = {}

on = True
while on:
    com = input('\n-Поиск \n-Создать \n-Удалить \n-Выйти \nВведите комманду: ')
    com = com.capitalize()
    if com == 'Поиск':
        f_name = input('Введите имя: ')
        if f_name in contacts:
            print('Контакт найден: ', contacts[f_name])
        else:
            print('Контакт не найден')
        continue
    if com == 'Создать':
        name = str(input("Введите имя контакта: "))
        phone = int(input("Веддите номер без '+, -' и скобок. Начните с 7: "))
        contacts[name] = phone
        print('Контакт ', name, '-', phone, 'добавлен.')
        continue
    if com == 'Удалить':
        f_name = input('Введите имя: ')
        if f_name in contacts:
            del contacts[f_name]
            print('Контакт удален')
        else:
            print('Контакт не найден')
        continue
    if com == 'Выйти':
        on = False
        break
    else:
        print('Комманда не найдена')