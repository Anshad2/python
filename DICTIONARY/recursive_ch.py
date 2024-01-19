text="ABCABBDE"
# print first recursive character
wc={}
for ch in text:
    if ch in wc:
        print("first recursive character is",ch)
        break
    else:
        wc[ch]=1

# non recursive character
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for k,v in wc.items():
    if(v==1):
        print(k)
print(wc)

# second recrusive character
text="ABBCDA"
wc={}
dup_char=[]
for ch in text:
    if ch in wc:
        wc[ch]+=1
        dup_char.append(ch)
    else:
        wc[ch]=1
print(dup_char[1])












