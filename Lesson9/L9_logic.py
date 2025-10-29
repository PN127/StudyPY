import random
import L9_interface

numder = random.randint(1, 100)

def guess():
    input_count = L9_interface.input_number()
    if input_count > numder:
        L9_interface.output_phrase('меньше')
        guess()
    elif input_count < numder:
        L9_interface.output_phrase('больше')
        guess()
    elif input_count == numder:
        L9_interface.output_phrase('угадал')
