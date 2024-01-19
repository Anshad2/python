# kangaroowords###interview question###
source_word="chicken"
target_word="hen"

source_word_lst=[ch for ch in source_word ]
print(source_word_lst)

target_word_lst=[ch for ch in target_word]
print(target_word_lst)

for ch in target_word_lst:
    if ch in source_word_lst:
        source_word_lst.remove(ch)
    else:
        print("not a kangaroo word")
        break
else:
    print("kangaroo word")

# simple method




# 
source_word="savage"
target_word="save"

s_lst1=[ch for ch in source_word]
print(s_lst1)
t_lst2=[ch for ch in target_word]
print(t_lst2)

for ch in t_lst2:
    if ch in s_lst1:
        s_lst1.remove(ch)
    else:
        print("not a kngarooword")
        break
else:
    print("kangarooword")

# 




word="pneumonoultramicroscopicsilicovolcanoconiosis"
# most frequent word
word_lst=[ch for ch in word]
print(word_lst)
for w in word:
    count=max(word,key=lambda w:word.count(w))
print(count)








