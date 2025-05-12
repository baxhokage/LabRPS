# Импортируем раннее созданые модули
from data_loader import random_arr
from data_saver import saver
from comb_sort import comb_sort
from tests import test_comb_sort

# Функция для ручного создания массива
def input_array(size):
    arr = [] 
    print(f"Введите {size} элементов массива:") 
    for _ in range(size): 
        num = int(input())
        arr.append(num)
    return arr

# Функция для вывода массива на экран
def print_array(arr):
    # Выводим элементы массива через пробел
    print("Массив:", ' '.join(map(str, arr)))

# Развилка
def main():
    while True:
        print ("Какую программу хотите использовать\n 1.Тест с рандомными значениями\n 2.Тест с вручную\n 3.Выйти из программы")
        cmd = int(input())
        match cmd:
            case 1:
                test_comb_sort()
            case 2:
                base()
            case 3:
                print("Досвидания!")
                break

# Ввод вручную массива
def base():
    size = int(input("Введите размер массива: "))
    arr = input_array(size)

    user_input = int(input("Сортировать по возрастанию? (1 - да, 0 - нет): "))
    if user_input == 1:
        reverse = False  # Сортировка по возрастанию
    else:
        reverse = True  # Сортировка по убыванию

    print("Несортированный массив:")
    print_array(arr)

    comb_sort(arr, reverse=reverse)

    print("Отсортированный массив:")
    print_array(arr)

    saver(arr, "output.txt")
    print("Отсортированные данные сохранены в 'sorted_output.txt'.")

# Точка входа в программу
if __name__ == "__main__":
    main()
