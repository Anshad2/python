# fizz_buzz
for number in range(1,101):
    if number%3==0 and number%5==0:
        print("fizz_buzz")
    elif  number % 5 ==0:
        print("fizz")
    elif number % 3==0:
        print("buzz")
    else:
        print(number)
