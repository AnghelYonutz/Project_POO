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

a = Animal("Vulpe", "eucariota", "animalia", "chordata", "mammalia", "canidae")
b = Animal("Ursul brun", "eucarioata", "animalia", "chordata", "mammalia", "ursidae")
c = Animal("Lupul", "eucariota", "animalia", "chordata", "mammalia", "canidae")
d = Animal("Cerb", "eucariota", "animalia", "chordata", "mammalia", "cervidae")

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






