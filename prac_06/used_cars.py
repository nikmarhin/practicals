"""CP1404/CP5632 Practical - Used cars."""

from prac_06.car import Car


def main():
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)


main()
