num1 = None
num2 = None

def calculation():
    op = input('Введите математическое действие: ')

    try:
        if op == '+':
            print ('Result: ', num1+num2)
        elif op == '-':
            print ('Result: ', num1-num2)
        elif op == '*':
            print ('Result: ', num1*num2)
        elif op == '/':
            print ('Result: ', num1//num2)
        else:
            print('Вы не указали действие')
            calculation()
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
        input_data()
    except Exception as e:
        print(f'Возникла ошибка во время калькуляции: {e}')
        calculation()

def input_data():
    global num1, num2 
    try:
        num1 = int(input('Веведите первое число: '))
        num2 = int(input('Веведите второе число: ')) 
        calculation()       
    except ValueError:
        print('Ошибка. Вы ввели не число.')
        input_data()
    except Exception as e:
        print('Возникла ошибка при сохранении вводе данных: ' + e)
    
    

input_data()
