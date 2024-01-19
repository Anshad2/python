# to split word by one by one
text="cricket updates Pakisthan won by 80 runs against netherlands"
words=text.split(" ")
for w in words:
    print(w)

# 
tweets="what a game,hats of both team..well don @benstokes38 @patcummins30 you have bought test cricket back to lif,love test cricket @theBarmyarmy,@cricketaus,@ecb_cricket"

words=tweets.split(" ")
for w in words:
    if w.startswith("@"):
        print(w)