item=["bat","ball","stumps","helmet","cricket","arc"]
# find longest word
longest_word=max(item,key=lambda w:len(w))
print(longest_word)

# smallest word
smallest_word=min(item,key=lambda w:len(w))
print(smallest_word)

# key used customized based what we need

# find largest word 
words=["red","green","blue","purpple","yellow"]
max_word=words[0]
for i in range(1,len(words)):
    curre_word=words[i]
    if len(curre_word) > len(max_word):
        max_word=curre_word
print(max_word)
    
# min_word

min_words=words[0]
for i in range(1,len(words)):
    curre_word=words[i]
    if len(curre_word) < len(min_words):
        min_words=curre_word
print(min_words)

# sum
sum=0
for i in range(0,len(words)):
    curre_word=words[i]
    sum=sum+len(curre_word)
print(sum)
