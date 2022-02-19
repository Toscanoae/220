"""
Name: Alex Toscano
hw5.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("enter a name(first last): ")
    split = name.split()
    print(split[1] + ", " + split[0])


def company_name():
    domain = input("enter a domain: ")
    split = domain.split(".")
    print(split[1])


def initials():
    num_stu = eval(input("how many students are in the class? "))
    for i in range(num_stu):
        name = input("what is the name of student " + str(i + 1) + "? ")
        split = name.split()
        print(split[0][0] + split[1][0])


def names():
    name = input("enter a list of names: ")
    split = name.split(", ")
    for i in split:
        initial = i.split()
        print(initial[0][0] + initial[1][0], end=" ")


def thirds():
    sentence = eval(input("enter the number of sentences: "))
    for i in range(sentence):
        sen = input("enter sentence " + str(i + 1) + ": ")
        print(sen[::3])


def word_average():
    sentence = input("enter a sentence: ")
    split = sentence.split()
    acc = 0
    for i in split:
        acc = acc + len(i)
    print(acc/len(split))


def pig_latin():
    latin = input("enter a sentence to convert to pig latin: ")
    lower = latin.lower()
    split = lower.split()
    for i in split:
        print(i[1:] + i[0] + "ay", end=" ".rstrip())


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    pig_latin()
