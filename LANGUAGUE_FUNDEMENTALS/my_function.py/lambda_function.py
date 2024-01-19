# to reduce the function
# only one line function multiple line statement not possible
# no def name automaticly return lamda num: condition
add=lambda n1,n2:n1+n2 
print(add(13,13))

# cube
cube=lambda num:num**3
print(cube(3))

# -ve or +ve
num_check=lambda num: "+ve" if num>0 else "-ve" if num<0 else "zero"
print(num_check(3))

# max_two
max_two=lambda n1,n2: n1 if n1>n2  else n2
print(max_two(9,8))

# odd even

odd_even=lambda num: "even" if num%2==0 else "odd"
print(odd_even(5))

# 
text="good evening all"#sorted based on length
words=text.split(" ")# split the word 3 
srt_words=sorted(words,key=lambda w:len(w),reverse=True)#based on length we use lambda 
print(srt_words)