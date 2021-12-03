input_string = input("Enter the array with numbers splitting by space : \n")
input_array = input_string.split(" ")
for i in range(len(input_array)):
    input_array[i] = int(input_array[i])


def heap_sort(Array):
    counter = 1
    build_heap_max(Array)
    for i in range(len(Array)-1, 0, -1):
        Array[0], Array[i] = Array[i], Array[0]
        counter += 1
        max_heapify(Array[:len(Array) - counter], 1)
    return Array


def build_heap_max(Array):
    for j in range(int(len(Array)/2), -1, -1):
        max_heapify(Array, j)


def max_heapify(Array, index):
    left = index * 2
    right = index + 2 + 1
    if left <= len(Array) and Array[left] > Array[index]:
        largest = left
    else:
        largest = index
    if right <= len(Array) and Array[right] > Array[index]:
        largest = right
    if largest != index:
        Array[index], Array[largest] = Array[largest], Array[index]
        max_heapify(Array, largest)


print(heap_sort(input_array))
