def test_sorting(array_size, num_tests):
    """Тестирует сортировку с указанным размером массива и числом тестов."""
    total_time = 0

    for _ in range(num_tests):
        array = random_arr(array_size)  # Генерация случайного массива
        start_time = time.time()  # Засекаем время
        comb_sort(array)  # Выполняем сортировку
        total_time += time.time() - start_time  # Считаем затраченное время

    avg_time = total_time / num_tests
    print(f"Среднее время сортировки массива размером {array_size}: {avg_time:.35f} секунд.")

if __name__ == "__main__":
    print("Тестирование с массивами разного размера")
    test_sorting(100, 100)    # 100 массивов размером 100
    test_sorting(1000, 100)   # 100 массивов размером 1000
    test_sorting(10000, 100)  # 100 массивов размером 10000