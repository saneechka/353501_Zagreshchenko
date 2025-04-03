from utils import get_integer_input, get_number_list, get_float_input
import time
import functools

def timing_decorator(func):
   
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@timing_decorator

def count_positives_greater_than_c(numbers, c):
    count = 0
    for num in numbers:
        if num > 0 and num > c:
            count += 1
    return count

@timing_decorator

def product_after_max_abs(numbers):
   
    if not numbers:
        return None
        
   
    max_abs_index = 0
    max_abs_value = abs(numbers[0])
    
    for i in range(1, len(numbers)):
        if abs(numbers[i]) > max_abs_value:
            max_abs_value = abs(numbers[i])
            max_abs_index = i

    if max_abs_index == len(numbers) - 1:
        return None
    

    product = 1
    for i in range(max_abs_index + 1, len(numbers)):
        product *= numbers[i]
    
    return product

def display_task5_submenu():

    print("\n--- Анализ списка чисел ---")
    print("1. Найти количество положительных элементов, больших C")
    print("2. Найти произведение элементов после максимального по модулю")
    print("0. Вернуться в главное меню")
    
    while True:
       
            choice = get_integer_input("Выберите пункт меню (0-2): ")
            if 0 <= choice <= 2:
                return choice
           


def run_task5():
    while True:
        print("\n--- Анализ списка чисел ---")
        print("1. Создать новый список чисел")
        print("0. Вернуться в главное меню")
        
        choice = get_integer_input("Выберите пункт меню (0-1): ", 0, 1)
        
        if choice == 0:
            break
        
     
        numbers = get_number_list()
       
        while True:
            print("\n--- Операции над списком ---")
            print("1. Найти количество положительных элементов, больших C")
            print("2. Найти произведение элементов после максимального по модулю")
            print("0. Вернуться к выбору списка")
            
            operation = get_integer_input("Выберите операцию (0-2): ", 0, 2)
            
            if operation == 0:
                break
            
            if operation == 1:
                c = get_float_input("Введите число C: ")
                count = count_positives_greater_than_c(numbers, c)
                print(f"Количество положительных элементов больших {c}: {count}")
            
            if operation == 2:
                product = product_after_max_abs(numbers)
                if product is not None:
                    print(f"Произведение элементов после максимального по модулю: {product}")
                else:
                    print("После элемента с максимальным модулем нет других элементов.")

