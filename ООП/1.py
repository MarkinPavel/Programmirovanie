ismport random

# ЭТАП 1 Инкапсуляция

class Monster:
    """Базовый класс монстра с приватными атрибутами"""

    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def show_status(self):
        print(f"[{self.__name}] HP: {self.__hp}")

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        return damage

    def attack_hunter(self, hunter):
        hunter.set_hp(hunter.get_hp() - self.__dmg)
        print(f"{self.__name} атакует {hunter.get_name()} и наносит {self.__dmg} урона!")


# ЭТАП 2 Наследование

class Zombie(Monster):

    def __init__(self, name="Зомби"):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        actual_damage = super().take_damage(damage)
        print(f"{self.get_name()} теряет конечность! Получено: {actual_damage}. HP: {self.get_hp()}")
        return actual_damage


class Vampire(Monster):

    def __init__(self, name="Дракула"):
        super().__init__(name, 80, 15)

    def take_damage(self, damage):
        absorbed = min(5, damage)
        actual_damage = damage - absorbed
        self.set_hp(self.get_hp() - actual_damage)
        print(f"{self.get_name()} поглощает {absorbed} урона! Получено: {actual_damage}. HP: {self.get_hp()}")
        return actual_damage


class Ghost(Monster):

    def __init__(self, name="Призрак"):
        super().__init__(name, 60, 20)

    def take_damage(self, damage):
        if random.random() < 0.3:
            print(f"{self.get_name()} уклоняется от атаки! HP: {self.get_hp()}")
            return 0
        else:
            actual_damage = super().take_damage(damage)
            print(f"{self.get_name()} получает {actual_damage} урона. HP: {self.get_hp()}")
            return actual_damage


class Werewolf(Monster):

    def __init__(self, name="Вервольф"):
        super().__init__(name, 100, 25)
        self.__transformed = False

    def take_damage(self, damage):
        actual_damage = super().take_damage(damage)
        print(f"{self.get_name()} получает {actual_damage} урона. HP: {self.get_hp()}")

        if not self.__transformed and self.get_hp() < 50:
            self.__transformed = True
            print(f"{self.get_name()} трансформируется!")

        return actual_damage


# ЭТАП 3 Полиморфизм

class Weapon:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def use(self, monster):
        pass


class SilverSword(Weapon):

    def __init__(self):
        super().__init__("Серебряный меч")

    def use(self, monster):
        damage = 30
        print(f"{self.get_name()} наносит удар! ")
        monster.take_damage(damage)


class HolyWater(Weapon):

    def __init__(self):
        super().__init__("Святая вода")

    def use(self, monster):
        damage = 20
        print(f"{self.get_name()} обжигает нечисть! ")
        monster.take_damage(damage)


class CrossbowBolt(Weapon):

    def __init__(self):
        super().__init__("Арбалет с болтом")

    def use(self, monster):
        damage = 25
        print(f"{self.get_name()} пронзает цель! ")
        monster.take_damage(damage)


# ЭТАП 4 Класс Охотника

class Hunter:

    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__weapons = []

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def add_weapon(self, weapon):
        self.__weapons.append(weapon)

    def show_inventory(self):
        print(f"\nИнвентарь {self.__name}:")
        for i, weapon in enumerate(self.__weapons, 1):
            print(f"  {i}. {weapon.get_name()}")

    def attack(self, weapon_index, monster):
        if 0 <= weapon_index < len(self.__weapons):
            weapon = self.__weapons[weapon_index]
            print(f"\n{self.__name} атакует {monster.get_name()} используя {weapon.get_name()}!")
            weapon.use(monster)
        else:
            print("Неверный индекс оружия!")

    def is_alive(self):
        return self.__hp > 0


# ЭТАП 5 Финальный бой
def run_game():
    hunter = Hunter("Ван Хельсинг")
    hunter.add_weapon(SilverSword())
    hunter.add_weapon(HolyWater())
    hunter.add_weapon(CrossbowBolt())

    monsters = [
        Zombie("Зомби"),
        Vampire("Дракула"),
        Ghost("Призрак"),
        Werewolf("Оборотень")
    ]

    for monster in monsters:
        print(f"Противник: {monster.get_name()} (HP: {monster.get_hp()})")

        while monster.is_alive() and hunter.is_alive():
            print(f"\n{hunter.get_name()} HP: {hunter.get_hp()} | {monster.get_name()} HP: {monster.get_hp()}")

            print("\nВыберите оружие (1-3):")
            hunter.show_inventory()

            try:
                choice = int(input("Ваш выбор: ")) - 1

                if 0 <= choice < 3:
                    hunter.attack(choice, monster)
                else:
                    print("Неверный выбор!")
                    continue

            except ValueError:
                print("Введите число!")
                continue

            if not monster.is_alive():
                print(f"\n{monster.get_name()} повержен!\n")
                break

            monster.attack_hunter(hunter)

            if not hunter.is_alive():
                print(f"\n{hunter.get_name()} пал в бою!")
                break

        if not hunter.is_alive():
            break

    if hunter.is_alive():
        print("Победа!")
        print(f"Оставшееся здоровье: {hunter.get_hp()}")
    else:
        print("Поражение!")

run_game()
