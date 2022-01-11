#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""
def hypotenuse(x,y):
    x = float(x)
    y = float(y)
    xy = x ** 2 + y ** 2
    yx = xy ** (1/2)
    return yx

x = input("the lenght of one side of a right triangle")
y = input("the lenght of the other side of a right triangle")
print(hypotenuse(x,y))

if __name__ == "__main__":
    x = input("the lenght of one side of a right triangle")
    y = input("the lenght of the other side of a right triangle")
    print(hypotenuse(x,y))
assert hypotenuse(6,8) == 10