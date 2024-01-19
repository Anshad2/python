text="hello hai hello hai"
words=text.split(" ")
print(words)
word_count={}
for ch in text:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
print(word_count)
