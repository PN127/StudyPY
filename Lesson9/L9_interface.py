def start_phrase():
    print('Я загадал число от 1 до 100. Попробуй отгадать его')

def input_number():
    input_count = int(input('Твое число: '))
    return input_count

def output_phrase(v):
    match v:
        case 'больше':
            text = 'Мое число больше'
        case 'меньше':
            text = 'Мое число меньше'
        case 'угадал':
            text = 'Молодец! Ты угадал.'
    print(text)