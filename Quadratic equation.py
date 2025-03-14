from math import sqrt

def square_root():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    if a == 0:
        print("Error: a cannot be 0 for a quadratic equation.")
        return

    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        x3 = max(x1, x2)
        x4 = min(x1, x2)
        print(x4)
        print(x3)
    elif d == 0:
        x1 = -b / (2 * a)
        print(x1)
    else:
        print("No real solutions")

square_root()
