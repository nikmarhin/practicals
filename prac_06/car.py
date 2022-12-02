"""CP1404/CP5632 Practical - Car class.
Estimated time - 60
Actual time - 75
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="limo", fuel=100):
        """Initialise a Car instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0  # We name this with a leading _ as it is "non-public"

        name_pieces = name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def __str__(self):
        """Return a string representation of a Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount: 20) -> 20:
        self.fuel += amount
        print(self.fuel)

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        distance = int(input("Distance: "))
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance


car1 = Car("Bugatti Chiron", 90)
# Creating a 2nd object using the Class construct
print(car1.name)
print(car1.fuel)
print(car1.first_name)
print(car1.last_name)

help(Car)