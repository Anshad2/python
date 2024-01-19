employee={"id":1000,"name":"ansh","department":"developer"}
# update department
employee["department"]="senior developer"
print(employee)

# if salary not prsent add salary 45000 else bonus 10000

if "salary" not in employee:
    employee["salary"]=45000
else:
    employee["salary"]+=10000
print(employee)

# 
text="pneumonoultramicroscopicsilicovolcanoconiosis"
character_count={}
for ch in text:
    if ch in character_count:
        character_count[ch]+=1
    else:
        character_count[ch]=1
print(character_count)

#

text="hello hai hello hai"
# word count hello =2 hai 2
words=text.split(" ")
print(words)
word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)