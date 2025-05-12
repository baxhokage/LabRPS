from comb_sort import comb_sort
from data_loader import random_arr

def test_comb_sort():
    print("Введите длину массива")
   
   # Создаем случайный массив указанной длины
    arr = random_arr(int(input()))
    
    user_input = int(input("Сортировать по возрастанию? (1 - да, 0 - нет): "))
    if user_input == 1:
        reverse = False  # Сортировка по возрастанию
    else:
        reverse = True  # Сортировка по убыванию

   
    # Выводим созданный тестовый массив
    print("Тестовый массив:", arr)
    
   # Сортируем массив методом Шелла 
    comb_sort(arr,reverse=reverse)
   # Выводим отсортированный  
    print("Отсортированный массив:", arr)


# Запускаем тестовую функцию, если этот файл выполняется как основная программа
if __name__ == "__main__":
    test_comb_sort()