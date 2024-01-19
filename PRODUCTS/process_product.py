from json import load
f=open("C:\\Users\\user\\Desktop\\my python\\products\\items.json","r",encoding="utf-8")
data=load(f)
print(len(data))

all_category={p.get("category")for p in data}
print(all_category)

# print electronic product
electronic_products=[p.get("title")for p in data if p.get("category")=="electronics"]
print(len(electronic_products))

# jwellery products
jewelery_products=[p.get("title")for p in data if p.get("category")=="jewelery"]
print(len(jewelery_products))

# costly product
costly_product=max(data,key=lambda d:d.get("price") )
print(costly_product)
