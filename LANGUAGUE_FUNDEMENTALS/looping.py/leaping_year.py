#leap year checking
starting_year=int(input("what is starting year"))
current_year=2023
i=starting_year
while(i<=current_year):
    if i% 400 == 0 and i%100==0 or i%4==0 and i% 100!=0:
        print(i)
    i+=1