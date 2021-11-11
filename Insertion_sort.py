input_string = input('Enter elements of a list separated by space : ')
input_list = input_string.split(' ')

for i in range(len(input_list)):
    input_list[i] = int(input_list[i])

output = [input_list[0]]
temp = 0
for i in range(1, len(input_list)):
    key = input_list[i]
    for j in range(i-1, -1, -1):
        if key > output[j]:
            output.insert(j+1, key)
            break
        elif j == 0:
            output.insert(0, key)


print(output)
