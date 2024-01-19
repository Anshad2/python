text="pneumonoultramicroscopicsilicovolcanoconiosis"
print(len(text))
print(type(text))
for ch in text:
    print(ch)

# vowels count fro the chara "a e i o u"
text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
for ch in text:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':# if ch in["a","e","i","o","u"]
        v_count+=1
print(f" vowel count = {v_count}")
print(len(text))



# 

tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"