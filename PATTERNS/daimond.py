#       *   
#      * *
#     * * * 
#    * * * *
#    * * * *
#     * * *
#      * *
#       *
# diamond




# 
def pyramid(rows):
    for i in range(rows):#row
        print(' '*(rows-i-1)+'*'*(i+1))
    for j in range(rows-1,0,-1):
        print(' '*(rows-j)+'*'*(j))
    print()


# or
def print_diamond(row):
    for i in range(row):
        print(" "*(row-i-1) +"*"*(2*i+1))
    for i in range(row-2,-1,-1):
        print(" "*(row-i-1) +"*"*(2*i+1))

print_diamond(5)