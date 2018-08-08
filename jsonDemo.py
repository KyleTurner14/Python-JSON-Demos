import json


class Person(object):
    name = ""
    age = 0
    color = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


def make_person(name, age, color):
    person = Person(name, age, color)
    return person


def main():

    name = input("Enter your name: ")

    age = input("Enter your age: ")

    color = input("Enter your favorite color: ")

    p = Person(name, age, color)

    print_as_JSON(p)

    return


def print_as_JSON(p):

    data = {"metadata": {"Response": "Gathered Data Successfully"},
            "person": {"name": p.name, "age": p.age, "color": p.color}}

    print(json.dumps(data, sort_keys=True, indent=4))

    return

main()