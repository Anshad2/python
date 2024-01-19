# # fibinocci
# pre_num=0
# curr_num=1
# print(f"{pre_num},{curr_num}",end=" ,")
# for i in range(1,13):
#     next=pre_num+curr_num
#     print(next,end=" ,")
#     pre_num=curr_num
#     curr_num=next



def fibonacci(n):
    pre_num = 0
    curr_num = 1
    fib_sequence = [pre_num, curr_num]

    for i in range(2, n):
        next_num = pre_num + curr_num
        fib_sequence.append(next_num)
        pre_num = curr_num
        curr_num = next_num

    return fib_sequence

# Generate and print the first 12 Fibonacci numbers
fib_numbers = fibonacci(12)
print(fib_numbers)


# # mul of 10
























