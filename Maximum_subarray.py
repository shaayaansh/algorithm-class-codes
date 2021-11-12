input_string = input("Enter the array with numbers separated by space : ")
input_array = input_string.split(' ')
for i in range(len(input_array)):
    input_array[i] = int(input_array[i])


def find_maximum_subarray(array, left, right):
    if left == right:
        return left, right, array[left]
    else:
        mid = int((left + right) / 2)

        (left_low, left_high, left_sum) = find_maximum_subarray(array, left, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(array, mid+1, right)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(array, left, mid, right)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(array, left, mid, right):
    negative_inf = -float('inf')
    left_sum = negative_inf
    sum = 0
    for i in range(mid, left-1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = negative_inf
    sum = 0
    for j in range(mid+1, right+1):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum+right_sum


print(find_maximum_subarray(input_array, 0, len(input_array)-1))
