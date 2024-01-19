mobile={"id":100,"name":"iphone","price":100000,"imei":12345,"processor":"apple"}

# all key value pairs
for k,v in mobile.items():# items = both key and values
    print(k,v)

# print name
print(mobile.get("name"))

# print price
print(mobile.get("price"))

# upadtes price as 85000

mobile["price"]=85000
print(mobile)

# remove imei
print(mobile.pop("imei"))
print(mobile)

# to add new keys value
mobile.update({"offer":1000})
print(mobile)

#or
mobile["offer"]=1000

# to chech a particular keyvalue  in the dictionary
mobile["price"]+=1000
print(mobile)

print("color"in mobile)