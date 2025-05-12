def comb_sort(arr, reverse=False):

    n = len(arr)
    gap = n
    shrink = 1.3  # ����������� ����������� ����������
    swapped = True
    
    while gap > 1 or swapped:
        # ������������ ����� ��������
        gap = max(1, int(gap / shrink))
        
        swapped = False
        
        for i in range(n - gap):
            # ��� ���������� �� �������� (reverse=True)
            if reverse:
                if arr[i] < arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
            # ��� ���������� �� ����������� (�� ���������)
            else:
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
                    
    return arr