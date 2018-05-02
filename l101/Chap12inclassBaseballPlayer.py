class BaseballPlayer:

    def __init__(self, name, jersey):
        self.name = name
        self.jersey = jersey

    def __str__(self):
        a = "Name = " + str(self.name) + " Jersey = " + str(self.jersey)
        return a


a = BaseballPlayer("Ted Williams", 11)

print(a)