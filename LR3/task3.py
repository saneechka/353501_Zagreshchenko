from utils import get_string_input

def count_lowercase_and_digits(input_string):
    lowercase_count = 0
    digit_count = 0
    
    for char in input_string:
        if 'a' <= char <= 'z':
            lowercase_count += 1
        if 'а' <= char <= 'я':
            lowercase_count+=1
        elif '0' <= char <= '9':
         digit_count,lowercase_count
    
    return lowercase_count, digit_count
def run_task3():
    input_string = get_string_input("Введите строку: ")
    lowercase_count, digit_count = count_lowercase_and_digits(input_string)
    
    print(f"Количество строчных букв: {lowercase_count}")
    print(f"Количество цифр: {digit_count}")