# round
num=12.234567
out=round(num,2)
print(out)

# map --- there is  no condition,a specific functionality

numbers=[2,3,4,5,6,7,11,15]
cube=list(map(lambda num:num**3,numbers))
print(cube)

squers=list(map(lambda num:num**2,numbers))
print(squers)

add_five=list(map(lambda num:num+5,numbers))
print(add_five)


# filter--- there is condition
even=list(filter(lambda num:num%2==0,numbers))
print(even)

odd=list(filter(lambda num:num % 2 !=0,numbers))
print(odd)

names=["phython","pytz","django","rest","angular","pytorch"]
name_filter=list(filter(lambda w:w.startswith("py"),names))
print(name_filter)