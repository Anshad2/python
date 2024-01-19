product={"code":1001,"name":"orange","prize":45}

# keys()
# values()
# items()
# upadte()
# get()
# pop()



# key() return all value
for k in product.keys():#key()
    print(k)

# get()#use get the key value to get specific one
print(product.get("prize"))

# values()
for v in product.values():
    print(v)

# both keys and product # items() 
for k,v in product.items():
    print(k,v)


# update
product["prize"]=50
print(product)
# or
product.update({"prize":50})
print(product)
# or
product.update({"name":"oranges"})
print(product)

# pop()=to remove
product.pop("prize")
print(product)

# to add keys:value
product.update({"offer":1000})
print(product)

# or
product["offer"]=1000
