
students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":2,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":3,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":4,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":5,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":6,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":7,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":8,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":9,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
    
]

# ? total number of students
print("total number students",len(students))

#? print all students name
for stud_name in students:
    print(stud_name.get("name"))

#or                                       
all_students_name=[stud_name.get("name")for stud_name in students]
print(all_students_name)

# ? exp >2
exp_students_name=[stud_name.get("name") for stud_name in students if stud_name.get("exp")>1]
print(exp_students_name)

# or
for stud_name in students:
 if stud_name.get("exp")>1:
     print(stud_name.get("name"))

# ? print  students name skill contain java and python 
# dict in side list(stud) main list(students)
for stud in students:
    if "java" in stud.get("skills") and "python" in stud.get("skills"):
        print(stud.get("name"))

# ? mca qul students
for stud in students:
    if stud.get("qualification")=="mca":
        print(stud.get("name"))
# or
mca_students_name=[stud.get("name")for stud in students if stud.get("qualification")=="mca"]
print(mca_students_name)

# ? highest exp students
max_exp_student=max(students,key=lambda s:s.get("exp"))
print(max_exp_student)

# ?most exp students
most_exp=max(students,key=lambda d:d.get("exp"))
highest_exp=most_exp.get("exp")
exp_studs=[stud.get("name") for stud in students if stud.get("exp")==highest_exp]
print(exp_studs)


# ? min exp
min_exp_student=min(students,key=lambda s:s.get("exp"))
print(min_exp_student)

#? students name with  more than two skills
skill_more_2_stud=[stud.get("name") for stud in students if len (stud.get("skills"))>2]
print(skill_more_2_stud)

# ? print student name start with j

start_j_with=[stud.get("name") for stud in students if stud.get("name").startswith("j") ]
# print(start_j_with)
# or
for stud in students:
    if stud.get("name").startswith("j"):
        print(stud.get("name"))


# ? most students selected skills
skills_count={}
for stud in students:
    skills=stud.get("skills")
    for sk in skills:
        if sk in skills_count:
            skills_count[sk]+=1
        else:
            skills_count[sk]=1
print(skills_count)

















