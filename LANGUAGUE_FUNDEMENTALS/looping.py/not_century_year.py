# print all non century year from starting to current year
starting_year=int(input("what is your starting year"))
current_year=2023
while (starting_year<=current_year):
    if starting_year % 100 != 0:
        print(starting_year)
    starting_year +=1