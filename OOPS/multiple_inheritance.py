# multiple_inheritance

class P1:
    def m1(self):
        print("inside m1")

class P2:
    def m2(self):
        print("inside m2")

class Child(P2,P1):
    pass

ch=Child()
ch.m1()
ch.m2()

# ######
class P1:
    def m1(self):
        print("inside m1")

class P2:
    def m1(self):
        print("inside m2")

class Child(P1,P2):# based on order check p1 satisfy print if not jumb to p2
    pass

ch=Child()
ch.n1()