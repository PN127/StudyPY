path = 'Lesson4/notes.txt'
file = open(path, 'a+', encoding='utf-8')
on = True

while on:
    com = input('\n-Записать\n-Показать\n-Очистить заметки\nВведите комманду: ')
    com = com.capitalize()
    if com == 'Записать':
        new_note = input('Напишите вашу заметку: ') + '\n'
        file.write(new_note)        
        continue
    if com == 'Показать':
        file.seek(0)
        print(file.read())       
        continue
    if com == 'Очистить':
        file.close()
        file = open(path, 'w', encoding='utf-8')
        file.close()
        file = open(path, 'a+', encoding='utf-8')
        print('Заметки удалены')       
        continue
    else:
        print('Комманда не найдена')

file.close()