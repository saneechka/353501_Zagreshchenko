from task1 import run_task1
from task2 import run_task2
from task3 import run_task3
from task4 import run_task4
from task5 import run_task5
from utils import get_integer_input
def display_menu():
    
    print("\n================= MENU ==================")
    print("1. Расчет косинуса с помощью ряда Тейлора")
    print("2. Подсчет чисел меньших 10")
    print("3. Подсчет строчных букв и цифр")
    print("4. Анализ текста")
    print("5. Анализ списка из чисел")
    print("0. Выход")
    
    while True:

            choice = get_integer_input("Выберите пункт меню (0-5): ", 0, 5)
            if 0 <= choice <= 5:
                return choice
         


def run_menu():
    
    while True:
        choice = display_menu()
        
        if choice == 0:
            print("Программа завершена. До свидания!")
            break
        elif choice == 1:
            run_task1()
        elif choice == 2:
            run_task2()
        elif choice == 3:
            run_task3()
        elif choice == 4:
            run_task4()
        elif choice == 5:
            run_task5()