input_string = input("Enter the numbers separating with space : \n")
input_array = input_string.split(' ')
for i in range(len(input_array)):
    input_array[i] = int(input_array[i])
temp = 0
for i in range(1, len(input_array)):
    key = input_array[i]
    for j in range(i-1, -1, -1):
        if input_array[j] > key:
            # print("comparing key :", key, "with element : ", input_array[j])
            input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
        else:
            break
    # print(input_array, i, "key is : ", key)

print(input_array)
