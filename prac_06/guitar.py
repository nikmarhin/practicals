"""
CP1404/CP5632 Practical 6
Guitar
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}), : $={self.cost}"

    def get_age(self):
        age = 2022 - self.year
        print(f"In 2022 the {self.name} is: {age}")
        return age

    def is_vintage(self, age):
        is_vintage = False
        if age > 50:
            is_vintage = True

    def __repr__(self):
        return str(self)


print(__name__)

if __name__ == '__main__':
    guitars = [Guitar("Fender Stratocaster '65 Reissue", 1965, 8054.20),
               Guitar("Mayones Regius Elements Air 7 string", 2006, 11340.50), Guitar("Gibson L-5", 1922, 16035.40)]
    is_vintage = [guitar for guitar in guitars if]

    g = Guitar
    print(g)
