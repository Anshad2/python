from json import load
f=open("C:\\Users\\user\\Desktop\\my python\\json_work\\students.json","r")
data=load(f)
print(data)

# all employees
for emp in data:
    print(emp.get("name"))

# all department
all_dep={dep.get("department") for dep in data}
print(all_dep)

# highest salry employee
hihest_salary=max(data,key=lambda d:d.get("salary"))
print(hihest_salary)

