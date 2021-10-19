#!python3
"""
Create a function that determines the largest number in a list of values and returns it.
1 input parameter:
list: the numbers to be checked for the largest value

return: float value of the largest number

Sample assertions:
assert largest([3,10,3]) == 10
"""
def largest(x):
    pass
    x = list(x)
    sortedx = sorted(x)
    biggestx = (max(sortedx))
    return biggestx


if __name__ == "__main__":
    x = input("enter list of values")
    print(largest(x))
    assert largest([10,50,100,3000.1]) == 3000.1