
# python collections
# collection object

                   
# list 

# tupple

# dictionary

# set 

# merge the lsit
str1="abc"
str2="defg"
lst = []
lst1 = []
lst.extend(str1)
lst1.extend(str2)
merged_list=list()
for i in range(max(len(lst),len(lst1))):
    for k in range(i,len(lst)):
        merged_list.append(lst[k])
        break
    for j in range(i,len(lst1)):
        merged_list.append(lst1[i])
        break
print(merged_list)