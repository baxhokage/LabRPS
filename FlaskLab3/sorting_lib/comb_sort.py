def comb_sort(arr, reverse=False):

    n = len(arr)
    gap = n
    shrink = 1.3  # Оптимальный коэффициент уменьшения
    swapped = True
    
    while gap > 1 or swapped:
        # Рассчитываем новый интервал
        gap = max(1, int(gap / shrink))
        
        swapped = False
        
        for i in range(n - gap):
            # Для сортировки по убыванию (reverse=True)
            if reverse:
                if arr[i] < arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
            # Для сортировки по возрастанию (по умолчанию)
            else:
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
                    
    return arr