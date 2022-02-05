"""
Name: Alex Toscano
hw3.py

Problem: using loops to do arithmetic

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    grades = eval(input("how many grades will you enter? "))
    acc = 0
    for i in range(grades):
        total = eval(input("enter grade: "))
        acc = acc + total
    print("average is", acc / grades)


def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("how much would you like to donate? "))
        acc = acc + tip
    print("total tips:", acc)


def newton():
    x = eval(input("What number do you want to square root? "))
    improvements = eval(input("How many times should we improve the approximation? "))
    approx = x
    for i in range(improvements):
        approx = (approx + (x / approx)) / 2
    print(approx)


def sequence():
    terms = eval(input("how many terms would you like? "))
    for i in range(terms):
        print(1 + (i // 2 * 2), end=" ")


def pi():
    n = eval(input("how many terms in series? "))
    acc = 1
    for i in range(n):
        num = 2 + ((i // 2) * 2)
        den = 1 + (((i + 1) // 2) * 2)
        acc = acc * (num / den)
    print(acc * 2)


if __name__ == '__main__':
    # average()
    # tip_jar()
    # newton()
    # sequence()
    pi()
