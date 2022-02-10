
'''Define classes for Espresso, Americano, Latte Macchiato, and Black Tea, Green Tea, and Yellow Tea. Think about building inheritance.
Define classes for Condiments like Milk and Sugar
Define a class for the vending machine's main controller
Define the main function that gets the input from the user and prints it out to the standard output.  '''


class Coffee:

    def __init__(self, temp, milk, sugar):
        self.temp = temp
        self.type = 'Coffee'
        self.milk = milk
        self.sugar = sugar

    def make(self):
        print(f"Made {self.temp} {self.type} with {self.milk} units of milk and {self.sugar} units of sugar.")


class Tea:
    def __init__(self, temp, milk, sugar):
        self.temp = temp
        self.type = 'Tea'

    def make(self):
        print(f"Made {self.temp} {self.type} with {self.milk} units of milk and {self.sugar} units of sugar.")


class Espresso(Coffee):
    def __init__(self):
        self.type = "Espresso"


class Americano(Coffee):
    def __init__(self):
        self.type = "Americano"


class LatteMacchiato(Coffee):
    def __init__(self):
        self.type = "Latte Macchiato"


class BlackTea(Tea):
    def __init__(self):
        self.type = "Black Tea"


class GreenTea(Tea):
    def __init__(self):
        self.type = "Green Tea"


class YellowTea(Tea):
    def __init__(self):
        self.type = "Yellow Tea"


class Milk:
    def __init__(self, unit):
        self.unit = unit


class Sugar:
    def __init__(self, unit):
        self.unit = unit


class Machine:
    def __init__(self):
        self.state = 'available'
        self.beverage = ''
        self.temp = ''
        self.milk = 0
        self.sugar = 0

    def brew(self, beverage, temp, milk, sugar):
        if self.state != 'available' or milk > 3 or milk < 0 or sugar > 3 or sugar < 0:
            print("Machine not available at the moment.")
        else:
            self.beverage = beverage
            self.temp = temp
            self.milk = milk
            print("Beverage in queue.")
            self.state = "not available"

        if beverage == 'Espresso':
            es = Espresso(self.temp, )
            es.make()
        elif beverage == 'Americano':
            am = Americano(self.temp)
        elif beverage == 'Americano':
            la = LatteMacchiato(self.temp)
        elif beverage == 'Americano':
            bl = BlackTea(self.temp)
        elif beverage == 'Americano':
            gr = GreenTea(self.temp)
        elif beverage == 'Americano':
            ye = YellowTea(self.temp)


def main():
    print("Starting Machine...")
    vending_machine = Machine()

    print('Machine Status: ' + vending_machine.state)

    beverage = input("Enter Espresso, Americano, Latte Macchiato, Black Tea, Green Tea, and Yellow Tea: ")
    if beverage in ['Espresso', 'Americano', 'Latte Macchiato', 'Black Tea', 'Green Tea', 'Yellow Tea']:
        print(beverage + ' ordered.')
    else:
        print("The type of beverage input is not available.")
    temp = input("Enter Cold or Hot")
    if temp == 'Hot':
        milk = input("Enter amount of milk between 0 to 3: ")
        sugar = input("Enter amount of sugar between 0 to 3: ")
    else:
        milk = 0
        sugar = 0

    vending_machine.brew(beverage, temp, milk, sugar)







if __name__ == "__main__":
    main()