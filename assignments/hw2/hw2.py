"""
Name: Alex Toscano
hw2.py

Problem: Solve with arithmetic with code.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper = eval(input("What is the upper bound:"))
    acc = 0
    for i in range(0, upper + 1, 3):
        acc = i + acc
    print(acc)


def multiplication_table():
    for i in range(1, 11):
        for l in range(1, 11):
            print(i * l, end=" ")
        print()


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    sides = (side_a + side_b + side_c) / 2
    area = math.sqrt(sides * (sides - side_a) * (sides - side_b) * (sides - side_c))
    print("area is", area)


def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    acc = 0
    for i in range(lower, upper + 1):
        acc = acc + i ** 2
    print(acc)


def power():
    base = eval(input("Enter Base: "))
    expo = eval(input("Enter Exponent: "))
    acc = 1
    for i in range(expo):
        acc = acc * base
    print(acc)


if __name__ == '__main__':
    # sum_of_threes()
    # multiplication_table()
    # triangle_area()
    # sum_squares()
    power()
