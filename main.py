class Animal:
    def __init__(self, animal, rasa, culoare, marime, domesticat):
        self.animal = animal
        self.rasa = rasa
        self.culoare = culoare
        self.marime = marime
        self.domesticat = domesticat

    def __str__(self):
        return "Aceasta este un/o {self.animal} de rasa {self.rasa}. Are culoare {self.culoare} si e de marime {self.marime}".format(self=self)

    def __eq__(self, other):
        if type(other) == Animal:
            return self.domesticat == other.domesticat
        else:
            return False

a = Animal("pisica", "persana", "alba", "mica", True)
b = Animal("caine", "beagle", "negru", "medie", True)
c = Animal("vulpe", "fennec", "gri", "medie", False)

print(a)
print(b)
print(c)

print(a == b)
print(b == c)
print(c == a)



