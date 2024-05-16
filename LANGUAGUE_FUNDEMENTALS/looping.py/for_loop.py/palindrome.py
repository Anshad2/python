def is_palindrome(num):
    num+=1
    while num>606:
        original_num = num
        reversed_num = 0
    
        while num > 0:
        # Extract the last digit of the number
            digit = num % 10
        # Append the digit to the reversed number
            reversed_num = (reversed_num * 10) + digit
        # Remove the last digit from the number
            num = num // 10
    
# #     # Compare the original number with the reversed number
# #         if original_num == reversed_num:
# #             result=""
# #             break
# #         num+=1
# #     # else:
# #     #     return False
# #     return result

# # # Example usage:
# # number = 606
# # print(is_palindrome(number))
# # # if is_palindrome(number):
# # #     print(f"{number} is a palindrome")
# # # else:
# # #     print(f"{number} is not a palindrome")


def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase
    # Remove non-alphanumeric characters
    s = ''.join(char for char in s if char.isalnum())
    
    # Initialize pointers
    start = 0
    end = len(s) - 1
    
    # Iterate until start pointer is less than end pointer
    while start < end:
        # If characters at start and end pointers are not equal, it's not a palindrome
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")



# def fibbanocci(n):
#     pre_num=0
#     curr=1
#     fibbanocci_seq=[pre_num,curr]
#     for i in range(2,n):
#      next=pre_num+curr
#      fibbanocci_seq.append(next)

#      pre_num=curr
#      curr=next
#     return fibbanocci_seq
# fib=fibbanocci(10)
# print(fib)