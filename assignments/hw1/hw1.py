"""
Name: Alex Toscano
hw1.py

Problem: Getting Started

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    tot_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shot_perc = shots_made / tot_shots * 100
    print("Shooting Percentage: ", shot_perc,  "%")


def coffee():
    coffee_lb = eval(input("How many pounds of coffee would you like? "))
    total = coffee_lb * 11.36 + 1.50
    print("Your total is:", round(total, 2))


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    k_to_m = kilometers / 1.61
    print("That's", k_to_m, "miles")


if __name__ == '__main__':
    calc_rec_area()
    calc_volume()
    shooting_percentage()
    coffee()
    kilometers_to_miles()
