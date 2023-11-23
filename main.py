class Animal:
    def __init__(self, animal, domeniu, regnu, branch, clasa, familia):
        self.animal = animal
        self.domeniu = domeniu
        self.regnu = regnu
        self.branch = branch
        self.clasa = clasa
        self.familia = familia

    def __str__(self):
        return "{self.animal} este un organism din domeniul {self.domeniu}, regnul {self.regnu}, incregatura {self.branch}, clasa {self.clasa}, din familia {self.familia}.".format(self=self)

    def __eq__(self, other):
        if type(other) == Animal:
            return self.familia == other.familia
        else:
            return False

a = Animal("Vulpea", "eucariota", "animalia", "chordata", "mammalia", "canidae")
b = Animal("Ursul brun", "eucarioata", "animalia", "chordata", "mammalia", "ursidae")
c = Animal("Lupul", "eucariota", "animalia", "chordata", "mammalia", "canidae")
d = Animal("Cerbul", "eucariota", "animalia", "chordata", "mammalia", "cervidae")

class Car(Animal):
    def __init__(self, animal, rasa, marime, culoare):
        self.sanimal = animal
        self.rasa = rasa
        self.marime = marime
        self.culoare = culoare
        super().__init__(animal)
    def __str__(self):
        return "Acesta este un/o {self.sanimal} de {self.rasa}, marime {self.marime}, de culoare {self.culoare}.".format(self=self)


print(a)
print(b)
print(c)
print(d)

print(a == b)
print(b == c)
print(c == a)
print(d == a)
print(d == b)
print(d == c)











