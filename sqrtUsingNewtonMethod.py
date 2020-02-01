# Write a static function sqrt to compute the square root of a nonnegative number c
# given in the input using Newton's method:
# ­ initialize t = c
# ­ replace t with the average of c/t and t
# ­ repeat until desired accuracy reached using condition Math.abs(t ­- c/t) > epsilon*t
# where epsilon = 1e­-15;

num = int(input("Enter the number for which you want to find the square root: "))


def squareroot(c):
    t = c
    while abs(t-(c/t))>((1e-15)*t):
        t = (c/t + t)/2
    return t    



print(squareroot(num))    