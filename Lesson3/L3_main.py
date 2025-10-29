import random

numder = random.randint(1, 100)

def guess():
    user_number = int(input('Твое число: '))
    if user_number > numder:
        print('Мое число меньше')
        guess()
    elif user_number < numder:
        print('Мое число больше')
        guess()
    elif user_number == numder:
        print('Молодец! Ты угадал.')

print('Я загадал число от 1 до 100. Попробуй отгадать его')
guess()