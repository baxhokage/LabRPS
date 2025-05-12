# Функция для сохранения массива в файл
def saver(arr, file="output.txt"): 
    # Отркываем файл в режиме записи и записываем туда элемента массива через \n
    with open(file, "w") as f:
        for _ in arr:
            f.write(f"{_}\n")