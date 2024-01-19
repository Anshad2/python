# print all century year from starting year to current year
starting_year=int(input("what is your starting century year"))
current_year=2023
while(starting_year<=current_year):
    if starting_year % 100 ==0:
      print(starting_year)
    starting_year+=1

