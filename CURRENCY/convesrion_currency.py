from json import load
f=open("C:\\Users\\user\\Desktop\\my python\\currency\\currency.json",encoding="utf-8")
data=load(f)
print(len(data))

# convert indian currency to other currenvcy rate

source_currency_code=input("enter the source currency code")
target_currency_code=input("enter the destination currency code")

amount=int(input("enter amount"))

conversion_rates=data.get("conversion_rates")
source_currency_code_rate=conversion_rates.get(source_currency_code)
destination_currency_code_rate=conversion_rates.get(target_currency_code)

# print(source_currency_code_rate)
# print(destination_currency_code_rate)
# print(conversion_rates)
res=(amount/source_currency_code_rate)*destination_currency_code_rate
print(res)

