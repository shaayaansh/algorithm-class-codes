input_string = input("Please enter the numbers with space in between: \n")
k = int(input("Please enter k : "))
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


def find_kth(arr, k):
    pivot = partition(arr, 0, len(arr)-1)
    if pivot == k:
        return arr[pivot]
    elif pivot < k:
        return find_kth(arr[pivot:], k - pivot)
    else:
        return find_kth(arr[:pivot], k)


print(find_kth(input_array, k-1))