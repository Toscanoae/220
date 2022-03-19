"""
Name: Alex Toscano
hw8.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_square(nums):
    filein = input("Enter name of infile: ")
    fileout = input("Enter name of outfile: ")
    infile = open(filein, "r")
    outfile = open(fileout, "w+")
    for line in infile:
        line = line.split()
        to_numbers(line)
        square_each(line)
        outfile.write("Sum of squares = " + str(sum_list(line)) + "\n")


def starter(weight, wins):
    weight = eval(input("Enter players weight: "))
    wins = eval((input("Enter players total wins: ")))
    if 150 <= weight < 160 and wins >= 5:
        print("Can start!")
    elif weight > 199 or wins > 20:
        print("Can start!")
    else:
        print("Sit on bench please!")


def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    # circle 1
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    # circle 2
    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    d = math.sqrt((circle_one.getX() - circle_two.getX()) ** 2 + (circle_one.getY() - circle_two.getY()) ** 2)
    if d <= circle_one.getRadius() + circle_two.getRadius():
        over = Text(Point(2, 6), "The circle overlaps!")
    else:
        under = Text(Point(2, 6), "The circle does not overlap!")


if __name__ == '__main__':
    # add_ten()
    # square_each()
    # sum_list()
    # to_numbers()
    # sum_of_square()
    # starter()
    # leap_year()
    circle_overlap()
    did_overlap()
