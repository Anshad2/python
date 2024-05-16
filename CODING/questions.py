# How do you reverse a string?
# How do you determine if a string is a palindrome?
# How do you calculate the number of numerical digits in a string?
# How do you find the count for the occurrence of a particular character in a string?
# How do you find the non-matching characters in a string?
# How do you find out if the two given strings are anagrams?
# How do you calculate the number of vowels and consonants in a string?
# How do you total all of the matching integer elements in an array?
# How do you reverse an array?
# How do you find the maximum element in an array?
# How do you sort an array of integers in ascending order?
# How do you print a Fibonacci sequence using recursion?
# How do you calculate the sum of two integers?
# How do you find the average of numbers in a list?
# How do you check if an integer is even or odd?
# How do you find the middle element of a linked list?
# How do you remove a loop in a linked list?
# How do you merge two sorted linked lists?
# How do you implement binary search to find an element in a sorted array?
# How do you print a binary tree in vertical order?
# amstrong
# prime,fact,leap
# vowelcount
# pangram
# kangaroo
# longerst palindromic string
# slicing
text = list("welcomepython")
vowels = "aeiou"
length = len(text)

print("Original text:", ''.join(text))

start = 0
end = length - 1

while start < end:
    start_character = text[start]
    end_character = text[end]
    
    if start_character in vowels and end_character in vowels:
        # Swap the vowels
        text[start], text[end] = text[end], text[start]
        start += 1
        end -= 1
    elif start_character not in vowels:
        start += 1
    elif end_character not in vowels:
        end -= 1

print("After swapping vowels:", ''.join(text))