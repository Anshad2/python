lst=[2,4,5,6,7,8,9]
squares=[]
for num in lst:
    sq=num**2
    squares.append(sq)
print(squares)
# or 
# in single method   =  [#return value for num in lst condition]
square=[num**2 for num in lst]
print(square)
# cube
cube=[num**3 for num in lst]
print(cube)
# evens number list
evens=[]
for num in lst:
    if num%2==0:
        evens.append(num)
print(evens)
# even by single line
even=[num for num in lst if num%2==0]
print(even)
# odd list
odd=[]
for num in lst:
     if num%2 !=0:
         odd.append(num)
print(odd)        
# odd by single line

odd=[num for num in lst if num%2!=0]
print(odd)


# num >5
num_gt_five=[num for num in lst if num>5]
print(num_gt_five)



# word

words=["apple","orrange","banana","mango","potatto"]
upper_case=[word.upper() for word in words ]
print(upper_case)

# print names length >6
#        return value                condition
name_gt_six=[word for word in words if len(word)>=6]
print(name_gt_six)



# 
lst=["red","green","blue","white","black","apple","ignore","under"]
# print words starting with vowels
# print word starting with consonent
start_with_vowel=[word for word in lst if word[0] in["a","e","i","o","u"]]#word[0].lower()
print(start_with_vowel)

# 
consonent=[word for word in lst if word[0] not in ["a","e","i","o","u"]]#word[0].lower()
print(consonent)






