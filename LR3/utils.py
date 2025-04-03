import random
def get_float_input(prompt, allow_negative=True):
    while True:
        try:
            value = float(input(prompt))
            if not allow_negative and value < 0:
                print("Error: Value must be non-negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user (Ctrl+C).")
            exit(0)
        except EOFError:
            print("\nOperation cancelled by user (EOF/Ctrl+Z).")
            exit(0)

def get_precision_input(prompt="Enter the precision (eps): "):
    while True:
        try:
            eps = float(input(prompt))
            if eps <= 0 or eps >= 1:
                print("Error: Precision must be between 0 and 1 (exclusive). Please try again.")
                continue
            return eps
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user (Ctrl+C).")
            exit(0)
        except EOFError:
            print("\nOperation cancelled by user (EOF/Ctrl+Z).")
            exit(0)

def get_integer_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Error: Value must be between {min_value} and {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user (Ctrl+C).")
            exit(0)
        except EOFError:
            print("\nOperation cancelled by user (EOF/Ctrl+Z).")
            exit(0)

def get_string_input(prompt):
    while True:
        try:
            value = input(prompt)
            if not value.strip():
                print("Error: Input cannot be empty. Please try again.")
                continue
            return value
        except KeyboardInterrupt:
            print("\nOperation cancelled by user (Ctrl+C).")
            exit(0)
        except EOFError:
            print("\nOperation cancelled by user (EOF/Ctrl+Z).")
            exit(0)

def readFromFile(promt):
    while True:
        try:
            filename = input(promt)
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    text = file.read()
                return text
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user (Ctrl+C).")
            exit(0)
        except EOFError:
            print("\nOperation cancelled by user (EOF/Ctrl+Z).")
            exit(0)
def get_number_list():
   
    print("\nВыберите способ создания списка:")
    print("1. Ввести список вручную")
    print("2. Сгенерировать случайный список")
    
    choice = get_integer_input("Выберите вариант (1-2): ", 1, 2)
    
    if choice == 1:
     
        while True:
            try:
                input_str = input("Введите список чисел через пробел: ")
                numbers = list(map(float, input_str.split()))
                return numbers
            except ValueError:
                print("Ошибка! Пожалуйста, введите корректные числа.")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user (Ctrl+C).")
                exit(0)
            except EOFError:
                print("\nOperation cancelled by user (EOF/Ctrl+Z).")
                exit(0)
    else:
        # Генерация через генератор
        size = get_integer_input("Введите размер списка: ", 1, 1000)
        min_val = get_float_input("Введите минимальное значение: ")
        max_val = get_float_input("Введите максимальное значение: ")
        
        if min_val > max_val:
            print("Минимальное значение больше максимального. Меняем местами.")
            min_val, max_val = max_val, min_val
            
        # Используем генератор для создания списка (всегда генерируем float)
        numbers = list(generator_number(size, min_val, max_val, False))
        
        # Выводим сгенерированный список
        print("\nСгенерированный список:")
     
            # Выводим весь список, если он достаточно короткий
        print(" ".join(f"{num:.2f}" for num in numbers))
       
            
      
        return numbers
def generator_number(size, min_val=-100, max_val=100, integer_only=False):
    for _ in range(size):
        if integer_only:
            yield random.randint(min_val, max_val)
        else:
            yield random.uniform(min_val, max_val)