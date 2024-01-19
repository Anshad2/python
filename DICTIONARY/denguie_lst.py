dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]
wc={}
for dist in dengue_list:
    if dist in wc:
        wc[dist]+=1
    else:
        wc[dist]=1

print(wc)

wc_srt=sorted(wc,key=lambda k:wc.get(k),reverse=True)
print(wc_srt)

# interview question

# 1=[a,b,c]
# 2=[d,e,f]
# 3=[g,h,i]
# 12=(a,d)(a,e)(a,f)(b,d)(b,e)(b,f)(c,d)(c,e)(c,f)
dials={"1":["a","b","c"],"2":["d","e","f"],"3":["g","h","i"]}

user_input="12"
main_list=[]
for ch in user_input:
    sub_list=dials.get(ch)
    main_list.append(sub_list)
print(main_list[0])
print(main_list[1])
