#                    path                        file name     mode
# f=open("\\Users\\user\\Desktop\\my python\\fileio\\colors.txt","w")
# f=open(path of folder,"mode")mode=r,w,append

# colors=["red","green","blue"]
# for c in colors:
#  f.write(c+"\n")

# f.write("hello")#to write 

# write all century years from 1800 into centrury years.text

# f=open("C:\\Users\\user\\Desktop\\my python\\fileio\\century_year.txt","w")
# for year in range(1800,2025):
#     if year% 100==0 :
#         f.write(str(year)+"\n")

# write all years from 1800 to 2024 in to yeras.txt
# f=open("C:\\Users\\user\\Desktop\\my python\\fileio\\years.txt","w")
# for year in range(1800,2025):
#     f.write(str(year)+"\n")


# read all years from years.txt and print leap year
# f=open("C:\\Users\\user\\Desktop\\my python\\fileio\\years.txt","r")
# for line in f:
#     year=int(line.rstrip("\n"))
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         print(year)

#read and write::: write all leap_years into leap_year.txt
read_path="C:\\Users\\user\\Desktop\\my python\\fileio\\years.txt"
write_path="C:\\Users\\user\\Desktop\\my python\\fileio\\leap_years.txt"
fw=open(write_path,"w")
fr=open(read_path,"r")
for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        fw.write(str(year)+"\n")

