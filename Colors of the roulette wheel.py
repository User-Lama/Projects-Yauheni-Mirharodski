x = int(input())
if x == 0:
    print("green")
elif (10 >= x >= 1) and (x % 2 == 0) or ((28 >= x >= 19) and (x % 2 == 0)):
    print("black")
elif (10 >= x >= 1) and (x % 2 != 0) or ((28 >= x >= 19) and (x % 2 != 0)):
    print("red")
elif (18 >= x >= 11) and (x % 2 == 0) or (36 >= x >= 29 ) and (x % 2 == 0):
    print("red")
elif(18 >= x >= 11) and (x % 2 != 0) or (36 >= x >= 29) and (x % 2 != 0):
    print("black")
else:
    print("Input error")