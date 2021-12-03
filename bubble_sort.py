input_string = input("Please enter an Array of numbers, splitting by space: \n")
input_array = input_string.split(" ")
for i in range(len(input_array)):
    input_array[i] = int(input_array[i])


def bubble_sort(Array):
    for i in range(1, len(Array)):
        for j in range(len(Array) - 1, i-1, -1):
            if Array[j] < Array[j-1]:
                Array[j], Array[j-1] = Array[j-1], Array[j]

    return Array


print(bubble_sort(input_array))
