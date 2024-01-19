 # linear method it is complex and time consuming

#     0  1 2  3 4 5
lst=[10,2,11,5,7,20]
#     low  mid    upp
element=5
i=0
is_present=False
while(i<=len(lst)):# by using while loop
  curr_element=lst[i]
  if curr_element==element:
    is_present=True
    break

  i+=1
print(is_present)

# by using for loop
for i in range(0,len(lst)):
  curr_element=lst[i]
  if curr_element==element:
    is_present=True
    break
print(is_present)

# the above method is done simply by binary method
lst=[10,2,11,5,7,20]
lst.sort()
element=int(input("enter element"))
is_present=False
low=0
upp=len(lst)-1

while(low<=upp):

  mid=(low+upp)//2
  if element==lst[mid]:
    is_present=True
    break
  elif element<lst[mid]:
    upp=mid-1
  elif element>lst[mid]:
    low=mid+1
print(is_present)


# low---------mid-----------upp
# element=list[mid]  True
#  element<list[mid]
#    upp=mid-1
# element>list[mid]
#    low=mid+1

