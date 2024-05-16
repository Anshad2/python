def max_zero_sequence_length(data_list):
    max_length = 0
    current_length = 0

    for num in data_list:
        if num == 0:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0

    return max_length
print(max)



print(f"value {x}")



# output = max_zero_sequence_length(data_list)
# print("Output:", output)


#  Python : inheritance, data structures, threading,oops
#  : find the median of two sorted arrays

data_list = [1, 0, 8, 0, 0, 4, 5, 0, 0, 0, 0]

frequency_dict = {}
for element in data_list:
    if element in frequency_dict:
        frequency_dict[element] += 1
    else:
        frequency_dict[element] = 1

print(frequency_dict)
print(max(frequency_dict))



# count taking

