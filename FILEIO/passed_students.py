# all students and failed students we creat a new file with passed students
# read  all names from all students and passed students
# then we creat a two set for all students and passed students
# the to get passed students we just minus from all students - failed students

all_stud=open("C:\\Users\\user\\Desktop\\my python\\fileio\\students.txt","r")
failed_stud=open("C:\\Users\\user\\Desktop\\my python\\fileio\\failed.txt","r")

all_student_set={st.rstrip("\n") for st in all_stud}
failed_stud_set={st.rstrip("\n") for st in failed_stud}

passed_students=all_student_set-failed_stud_set
print(passed_students)
    
