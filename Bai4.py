import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
S=(a+b+c)/2
print("Dien tich="+str(math.sqrt(S*(S-a)*(S-b)*(S-c))))