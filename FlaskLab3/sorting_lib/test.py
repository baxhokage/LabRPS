from comb_sort import comb_sort
from data_loader import random_arr

def test_shell_sort(test_size):
   
   # ������� ��������� ������ ��������� �����
    arr = random_arr(int(test_size))
    reverse = False  # ���������� �� �����������
    comb_sort(arr,reverse=reverse)
   # ������� ���������������  