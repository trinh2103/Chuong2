import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
S=(a+b+c)/2
print("Dien tich="+str(math.sqrt(S*(S-a)*(S-b)*(S-c))))