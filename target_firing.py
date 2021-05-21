#! venv/binpython3
class Ship(object):
    def __init__(self, name="Ship", hp=0, armor=0, damage=0):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def take_damage(self, weapon):
        self.hp -= (weapon - self.armor)
        print(f'Enemy took a {weapon} point hit and is down to {self.hp}')

    def fire(self, weapon):
        print(f'Enemy fired a {weapon} point hit you are down to {self.hp}')


class BirdOfPrey(Ship):
    def __init__(self, name=None, hp=0, armor=0, damage=0):
        super().__init__(name, hp, armor, damage)


class BattleCruiser(Ship):
    def __init__(self, name=None, hp=0, armor=0, damage=0):
        super().__init__(name, hp, armor, damage)


def do_battle(me):
    num_ships = 1  # int(input("Enter number of ships: "))
    print(f"Number of ships: {num_ships}")
    enemy = Ship()
    for i in range(num_ships):
        attr = [i for i in input().split()]  # [i for i in ['Cruiser', 1000, 0, 0]]  #
        if 'f' in attr[0].lower():
            enemy = BirdOfPrey(attr[0], int(attr[1]), int(attr[2]), int(attr[3]))
        else:
            enemy = BattleCruiser(attr[0], int(attr[1]), int(attr[2]), int(attr[3]))

    # they attack first
    me.hp -= enemy.damage


if __name__ == "__main__":
    starfleet = Ship("NCC1701-D", 5000, 0, 10)
    do_battle(starfleet)
    if starfleet.hp <= 0:
        print("FLEE")
    else:
        print(starfleet.hp)
