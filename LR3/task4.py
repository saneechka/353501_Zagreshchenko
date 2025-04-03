from utils import get_integer_input
def is_consonant(char):
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return char in consonants

def has_consecutive_duplicate_letters(word):
    for i in range(len(word) - 1):
        if word[i].lower() == word[i + 1].lower():
            return True
    return False

def count_words_starting_with_consonant(words):
    count = 0
    for word in words:
        clean_word = word.strip('.,!?;:()[]{}"\'«»')
        if clean_word and is_consonant(clean_word[0]):
            count += 1
    return count

def find_words_with_consecutive_duplicates(words):
    result = []
    for i, word in enumerate(words, 1):
        clean_word = word.strip('.,!?;:()[]{}"\'«»')
        if clean_word and has_consecutive_duplicate_letters(clean_word):
            result.append((word, i))
    return result

def clean_words_for_sorting(words):
    clean_list = []
    for word in words:
        clean_word = word.strip('.,!?;:()[]{}"\'«»')
        if clean_word:
            clean_list.append(clean_word)
    return clean_list

def display_task4_submenu():

    print("1. Определить число слов, начинающихся с согласной")
    print("2. Найти слова с двумя одинаковыми буквами подряд и их номера")
    print("3. Вывести слова в алфавитном порядке")
    print("4. Выполнить все операции")
    print("0. Вернуться в главное меню")
    
    while True:
        
            choice = get_integer_input("Выберите пункт меню (0-4): ", 0, 4)
            if 0 <= choice <= 4:
                return choice
           


def run_task4():
   
        
        with open("TextForTask4.txt", "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()
        
        while True:
            choice = display_task4_submenu()
            
            if choice == 0:
               
                break
                
          
            if choice in [1, 2, 3]:
                print("\nТекст из файла:")
                print(text)
                print("\nРезультаты анализа:")
            
            if choice == 1 :

                consonant_count = count_words_starting_with_consonant(words)
                print(f"a) Количество слов, начинающихся с согласной: {consonant_count}")
            
            if choice == 2:

                duplicate_words = find_words_with_consecutive_duplicates(words)
                print("b) Слова с двумя одинаковыми буквами подряд и их номера:")
                if duplicate_words:
                    for word, position in duplicate_words:
                        print(f"   Слово: {word}, позиция: {position}")
                else:
                    print("   Таких слов не найдено")
            
            if choice == 3:
          
                clean_word_list = clean_words_for_sorting(words)
                unique_words = list(set(clean_word_list))
                sorted_words = sorted(unique_words, key=lambda s: s.lower())
                print("c) Слова в алфавитном порядке:")
                print("   " + ", ".join(sorted_words))
                
