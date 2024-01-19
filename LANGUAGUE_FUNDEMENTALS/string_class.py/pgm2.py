text="pneumonoultramicroscopicsilicovolcanoconiosis"
con_count=0
for ch in text:
    if ch not in["a","e","i","o","u"]:# consonant count means letter without vowels
      if ch.isalpha():
       con_count+=1
print(f"consonent is = {con_count}")
print(len(text))
