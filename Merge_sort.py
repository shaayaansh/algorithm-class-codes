import math


def merge_sort(array, left, right):
    if left < right:
        q = math.floor((left + right)/2)
        merge_sort(array, left, q)
        merge_sort(array, q+1, right)
        merge(array, left, q, right)
    pass


def merge(array, left, q, right):
    left_array = array[left:q+1]
    right_array = array[q+1:right+1]
    right_array_index = 0
    left_array_index = 0
    for i in range(len(array)):
        if left_array[left_array_index] >= right_array[right_array_index]:
            array[i] = left_array[left_array_index]
            left_array_index += 1
            if left_array_index == len(left_array) - 1:
                array[i:len(array)] = right_array[right_array_index:len(right_array)]
                break
        else:
            array[i] = right_array[right_array_index]
            right_array_index += 1
            if right_array_index == len(right_array) - 1:
                array[i:len(array)] = left_array[left_array_index:len(left_array)]
                break


input_string = input("Enter the numbers separating with space: \n")
input_array = input_string.split(' ')
for i in range(len(input_string)):
    input_array[i] = int(input_array[i])
merge_sort(input_array, 0, len(input_array)-1)
print(input_array)