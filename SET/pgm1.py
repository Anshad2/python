insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopy","lalu"}
mohanlal_following={"prithvi","vijay","lalu"}
suuggetions_for_mohanlal=insta_users.difference(mohanlal_following)
suuggetions_for_mohanlal.discard("mohanlal")
print(suuggetions_for_mohanlal)

dq_friend={"prithvi","fahad","sureshgopy","lalu"}
mutual_frnds=mohanlal_following.intersection(dq_friend)
print(mutual_frnds)


orders1={"cb","tika","fishfry","friedrice","vb","gheeroast"}
orders2={"cb","friedrice","nan","upma","vegmeals","idly"}
# elements in orders1 and orders2 but not in both 
# orders1 union orders2 - orders1 intersection orders2
order_union=orders1.union(orders2)
order_inter=orders1.intersection(orders2)
new_order=order_union.difference(order_inter)
print(new_order)
# symmetric diffrence
new_order=orders1.symmetric_difference(orders2)
print(new_order)