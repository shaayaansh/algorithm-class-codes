input_string = input("Please Enter the numbers with space between them : \n")
input_array = input_string.split(" ")
for i in range(len(input_array)):
    input_array[i] = int(input_array[i])


def partition(arr, l, r):
    pivot = arr[r]
    left_index = l - 1
    for i in range(l, r):
        if arr[i] <= pivot:
            left_index += 1
            arr[left_index], arr[i] = arr[i], arr[left_index]
    arr[left_index+1], arr[r] = arr[r], arr[left_index+1]
    return left_index + 1


def quick_sort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, pivot+1, r)
        quick_sort(arr, l, pivot-1)
    return arr


print("FINAL ARRAY IS : ", quick_sort(input_array, 0, len(input_array)-1))

