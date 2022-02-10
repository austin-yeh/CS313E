class Coffee:
    def __init__(self, temperature):
        self.name = 'Coffee'
        self.temperature = temperature

    def __str__(self):
        return self.temperature + ' ' + self.name


class Tea:
    def __init__(self, temperature):
        self.name = 'Tea'
        self.temperature = temperature

    def __str__(self):
        return self.temperature + ' ' + self.name


class Espresso(Coffee):
    def __init__(self, temperature):
        super().__init__(temperature)
        self.name = 'Espresso'


class Americano(Coffee):
    def __init__(self, temperature):
        super().__init__(temperature)
        self.name = 'Americano'


class LatteMocchiato(Coffee):
    def __init__(self, temperature):
        super().__init__(temperature)
        self.name = 'Latte Mocchiato'


class BlackTea(Tea):
    def __init__(self, temperature):
        super().__init__(temperature)
        self.name = 'Black Tea'


class GreenTea(Tea):
    def __init__(self, temperature):
        super().__init__(temperature)
        self.name = 'Green Tea'


class YellowTea(Tea):
    def __init__(self, temperature):
        super().__init__(temperature)
        self.name = 'Yellow Tea'


class Milk:
    def __init__(self):
        self.unit = 0

    def set_unit(self, unit):
        self.unit = unit

    def __str__(self):
        return str(self.unit) + ' units of milk'


class Sugar:
    def __init__(self):
        self.unit = 0

    def set_unit(self, unit):
        self.unit = unit

    def __str__(self):
        return str(self.unit) + ' units of sugar'


class Machine:
    def __init__(self):
        self.state = 'available'
        print('Machine status', self.state)

    def add(self, addition):
        print('Added', addition)

    def brew(self, name, temperature, milk_unit, sugar_unit):
        self.state = 'unavailable'
        print('Machine status', self.state)
        if name == 'Espresso':
            drink = Espresso(temperature)
        elif name == 'Americano':
            drink = Americano(temperature)
        elif name == 'Latte Mocchiato':
            drink = LatteMocchiato(temperature)
        elif name == 'Black Tea':
            drink = BlackTea(temperature)
        elif name == 'Green Tea':
            drink = GreenTea(temperature)
        elif name == 'Yellow Tea':
            drink = YellowTea(temperature)
        else:
            print("Drink not defined")
            self.state = 'available'
            print('Machine status', self.state)
            return

        milk = Milk()
        milk.set_unit(milk_unit)
        sugar = Sugar()
        sugar.set_unit(sugar_unit)
        self.add(drink)
        self.add(milk)
        self.add(sugar)

        print(f"Brewed {drink} with {milk} and {sugar}.\n")
        self.state = 'available'
        print('Machine status', self.state)
        return


def main():
    print('Starting machine...\n')
    machine = Machine()

    while True:
        while True:
            name = input('Enter the type of drink you want today: ')
            if name not in ['Espresso', 'Americano', 'Latte Mocchiato', 'Black Tea', 'Green Tea', 'Yellow Tea']:
                print('Drink not available.\n')
                continue
            break
        while True:
            temperature = input('Do you want your drink hot or cold? ')
            if temperature not in ['hot', 'cold']:
                print('Temperature not available.\n')
                continue
            break
        milk, sugar = 0, 0
        if temperature == 'hot' and name in ['Americano', 'Espresso', 'Latte Mocchiato']:
            while True:
                milk = float(input('Enter amount of milk: '))
                sugar = float(input('Enter amount of sugar: '))
                if not (0 <= milk <= 3 and 0 <= sugar <= 3):
                    print('Units not available.\n')
                    continue
                break
        machine.brew(name, temperature, milk, sugar)


if __name__ == "__main__":
    main()
