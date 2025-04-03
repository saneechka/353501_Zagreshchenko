from utils import get_integer_input
def count_numbers_less_than_10():
   
    count = 0
    while True:
      

            num = get_integer_input("Введите число (100 для выхода): ")
            if num == 100:
                break
            if num < 10:
                count += 1
        
    
    return count

def run_task2():
    result = count_numbers_less_than_10()
    print(f"Количество введенных чисел меньше 10: {result}")

