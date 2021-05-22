#! venv/binpython3
from collections import OrderedDict


class Ship(object):
    def __init__(self, name="Ship", hp=0, shields=0, damage=0):
        self.name = name
        self.hp = hp
        self.shields = shields
        self.damage = damage
        self.is_threat = True

    def deal_damage(self, target):
        if target.name.upper() == "FIGHTER":
            damage = self.damage * 2 - target.shields
        elif target.name.upper() == "CRUISER":
            damage = self.damage - target.shields

        target.hp -= damage if damage >= 1 else 1


class Fighter(Ship):
    def __init__(self, name=None, hp=0, shields=0, damage=0):
        super().__init__(name, hp, shields, damage)


class Cruiser(Ship):
    def __init__(self, name=None, hp=0, shields=0, damage=0):
        super().__init__(name, hp, shields, damage)


def get_threat_level(enemies):
    # general threat flag; True if 1 or more enemies is a threat
    for enemy in enemies:
        if enemies[enemy].is_threat:
            return True
    return False


def get_enemies():
    # collect a dictionary of enemy ships
    num_ships = int(input())
    enemies = OrderedDict()
    for i in range(num_ships):
        attr = [i for i in input().split()]  # [i for i in ['Cruiser', 1000, 0, 0]]  #
        if 'f' in attr[0].lower():
            enemy = Fighter(attr[0], int(attr[1]), int(attr[2]), int(attr[3]))
        else:
            enemy = Cruiser(attr[0], int(attr[1]), int(attr[2]), int(attr[3]))

        enemies.update({i: enemy})
    return enemies


def do_battle_with_(combatant):
    """
    :param: me
    :returns: n/a
    """
    enemies = get_enemies()

    general_threat = True
    while general_threat:
        general_threat = get_threat_level(enemies)

        most_powerful_attack = 0
        most_powerful_ship = None
        for k, enemy in enemies.items():
            if enemy.is_threat:
                combatant.hp -= enemy.damage
                if enemy.damage > most_powerful_attackt:
                    most_powerful_ship = enemy

        # every enemy (that can) has attacked in
        # this round and the player can now attack
        # the most powerful ship
        combatant.deal_damage(most_powerful_ship)
        if enemy.hp < 0:
            # 'eliminate' the target
            enemy.is_threat = False


if __name__ == "__main__":
    starfleet = Ship("NCC1701-D", 5000, 0, 10)
    do_battle_with_(starfleet)
    if starfleet.hp <= 0:
        print("FLEE")
    else:
        print(starfleet.hp)
