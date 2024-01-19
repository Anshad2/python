# print runner up score list=[2,3,6,6,5,4]
list=[2,3,6,6,5,4]
print(sorted(list))
sorted_score=sorted(set(list),reverse=True)
second_highest=sorted_score[1]
print(second_highest)

records=[]
print(sorted(records))

sorted_records=sorted(set(records),reverse=True)
second_score=sorted_score[1]
print(second_highest)