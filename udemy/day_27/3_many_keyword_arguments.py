def calculate(n, **kwargs):
    # type dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


calculate(4, add=3, multiply=5)

print(calculate(5, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # we use get instead kw[""] to avoid errors if not present
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)

my_car = Car(model="GT-R", color="Red")
print(my_car.color + " - " + my_car.model)
