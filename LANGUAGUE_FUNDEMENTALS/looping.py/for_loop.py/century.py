# leap year from 1800 to 2024
start_year=1800
end_year=2025
for year in range(start_year,end_year):
    if (year % 4==0 and year %100!=0 or year %400==0 and year%100==0):
        print(year)

# century year
start_year=int(input("year is"))
end_year=2024
for year in range(start_year,end_year):
    if year%100==0:
        print(year)
