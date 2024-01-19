# nested collection

vehicle=[
    {"id":1,"name":"passionpro","brand":"hero","price":100000},
    {"id":2,"name":"xplus","brand":"hero","price":140000},
    {"id":3,"name":"trump","brand":"trump","price":200000},
    {"id":4,"name":"hunter","brand":"ola","price":170000},
    {"id":5,"name":"ola","brand":"honda","price":220000},
    {"id":6,"name":"ather 400","brand":"ather","price":180000}
]

# print all vehicle name
for bike in vehicle:
    print(bike.get("name"))
# print brand name
for bike in vehicle:
    print(bike.get("brand"))

# brand hero bike
for bike in vehicle:
    if bike.get("brand")=="hero":
     print(bike.get("name"))

# bike avaivle under 150000
# costly bike

for bike in vehicle:
   if bike.get("price")<150000:
      print(bike.get("name"))

# costly bike                      dict
costly_bike=max(vehicle,key=lambda d:d.get("price"))
print(costly_bike)

# low_cost bike
low_cost=min(vehicle,key=lambda d:d.get("price"))
print(low_cost)


