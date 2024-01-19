# random number
# Import the random module, and display a random number between 1 and 9:
# produce random output
import random
print(random.randrange(1,9))

# head or tile
 
import random
random_side=random.randint(0,1)
if random_side==1:
    print("head")
else:
    print("tail")