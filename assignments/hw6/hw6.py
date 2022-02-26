"""
Name: Alex Toscano
hw6.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math


def cash_converter():
    integer = eval(input("enter an integer: "))
    print("That is", '${:.2f}'.format(integer))


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    acc = ""
    for i in message:
        i = ord(i)
        i = i + key
        new = chr(i)
        acc = acc + new
    print(acc)


def sphere_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area


def sphere_volume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


def sum_n(number):
    acc = 0
    for i in range(number):
        acc = acc + (i + 1)
    return acc


def sum_n_cubes(number):
    acc = 0
    for i in range(number + 1):
        acc = acc + (i ** 3)
    return acc


def encode_better():
    message = input("enter a message: ")
    keyword = input("enter a key: ")
    acc = ""
    for i in range(len(message)):
        nx = ord(message[i]) - 65
    print(nx)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    encode_better()
    pass
