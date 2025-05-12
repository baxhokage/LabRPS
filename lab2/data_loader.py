import random

# Функция для загрузки данных
def random_arr(size, min=0, max=100):
    # Генерируем массив из _ рандомных чисел в диапозоне min - max
    return [random.randint(min, max) for _ in range(size)]