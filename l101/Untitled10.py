class Person:
    first_name=""
    last_name=""
    age = ""
    def __init__(self, age):
        self.first_name = age

    def __set_name__(self, first_name):
        self.first_name = first_name

    def __set_last_name__(self, last_name):
        self.last_name = last_name

    def __str__(self):
        return "last_name = " + str(self.last_name) + " first_name"


me = Person(2)
me.__set_last_name__("Smith")

Person.__set_last_name__(me,"Smith")

print(me)