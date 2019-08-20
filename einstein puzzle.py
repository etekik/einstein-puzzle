print("""This is a puzzle favored by Einstein. You will be asked to enter
a three digit number, where the hundred's digit differs from the
one's digit by at least two. The procedure will always yield 1089
""")

ABC = input("Give me a number: ")
C = int(ABC) % 10
B = int((int(ABC) / 10) % 10)
A = int((int(ABC) / 10 ** 2) % 10)
CBA = int("{}{}{}".format(C, B, A))
if (CBA > int(ABC)):
    XYZ = (CBA) - int(ABC)
else:
    XYZ = int(ABC) - (CBA)
Z = int(XYZ) % 10
Y = int((int(XYZ) / 10) % 10)
X = int((int(XYZ) / 10 ** 2) % 10)
ZYX = int("{}{}{}".format(Z, Y, X))
Total = XYZ + ZYX
print("For the number: {} the reverse number is: {}".format(ABC,CBA))
print("The difference between {} and {} is {}".format(ABC, CBA, XYZ))
print("The reverse difference is: ",ZYX)
print("The sum of {} and {} is: {}".format(XYZ, ZYX, Total))






