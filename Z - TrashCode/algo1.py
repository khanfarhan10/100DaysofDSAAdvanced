"""
cd G:\GitLab\pdf_extraction\ModularInsurance
python algo1.py
"""
import sys
import random

sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())


def merge_sort(arr,n=None,pivot_index=None):
    """Returns sorted array"""
    n = len(arr) if n is None else n
    if n==1:
        return arr
    if n==2:
        a = arr[0]
        b = arr[1]
        srt = arr if a<b else arr[::-1]
        return srt 
    pivot_index = int(n/2)-1 if pivot_index is None else pivot_index
    # pivot_element = arr[pivot_index]

    left_arr = arr[:pivot_index]
    right_arr = arr[pivot_index:]

    left_sorted = merge_sort(left_arr, len(left_arr)) 
    right_sorted = merge_sort(right_arr, len(right_arr))

    len_left = len(left_sorted)
    len_right = len(right_sorted)

    i = 0
    j = 0
    big_old_arr = []
    while True:
        if i==len_left or j == len_right:
            break
        elif left_sorted[i] > right_sorted[j]:
            big_old_arr.append(right_sorted[j])
            j+=1
        else:
            big_old_arr.append(left_sorted[i])
            i+=1
    return big_old_arr

if __name__ == "__main__":
    arr = [4,8,1,5,7]
    print(merge_sort(arr))

if __name__ == "__main__2":

    a = "FarhanHaiKhan"
    sample_space = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

    details = dict()
    for each_letter in sample_space:
        if each_letter in a:
            details[each_letter] = a.count(each_letter)
        else:
            details[each_letter] = 0

    for key in details:
        val = details[key]
        if not val== 0:
            print(key, val)
    

