# string="abracadabra"

# # position=5

# # insert=k

# string1=""
# string=list("abracadabra")

# string.insert(5,"k")

# print(string1.join(string))



# runner up

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split())) 
#     unique_arr = list(set(arr))
#     unique_arr.sort(reverse=True)
#     if len(unique_arr) < 2:
#         print("There is no runner-up score.")
#     else:
#         print(unique_arr[1])


stringx="hello world"

words = stringx.split()

words = [word.capitalize() for word in words]

result = ' '.join(words)

print(result)


# str

result =stringx.replace('h','H').replace('w','W')

print(result)






