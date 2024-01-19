from json import load
f=open("C:\\Users\\user\\Desktop\\my python\\rest_countries\\data.json","r",encoding="utf-8")
data=load(f)
print(len(data))

# all country names
# all_country=[country.get("name") for country in data]
# print(all_country)

# print all independent country name
# all_independent_country=[country.get("name")for country in data if country.get("independent")==True]
# print(all_independent_country)

# print all regions
# all_regions={country.get("region" )for country in data}
# print(all_regions)

# all asian country
# all_asian_country=[country.get("name")for country in data if country.get("region")=="Asia"]
# print(all_asian_country)

# capital of ukrain
# 

# all country name and capital
# countries_capital=[(country.get("name"),country.get("capital"))for country in data]
# print(countries_capital)


# print all countryname and currency name
# for country in data:
#     if "currencies" in country:
#         currency_data=country.get("currencies")[0]
#         print(currency_data.get("name"),",",country.get("name"))

# india border sharing countries
# india_borders=[country.get("borders")for country in data if country.get("name")=="India"][0]
# print(india_borders)
# border_name=[country.get("name")for country in data if country.get("alpha3Code") in india_borders]
# print(border_name)

# borders more than 4
# for country in data:
#     if "borders" in country and len(country.get("borders"))>4:
#         print(country.get("name"))

