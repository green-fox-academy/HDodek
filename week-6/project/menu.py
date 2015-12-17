from random import randint

class MenuItem():
    def __init__(self, num, name, action):
        self.num = num
        self.name = name
        self.action = action

class Menu():
    def __init__(self, items):
        self.items = items

    def choose(self, number):
        for item in self.items:
                if item.num == number:
                    return item.action()

    def printMenu(self):
        for item in self.items:
            print(item.num, item.name)

    def user_input(self):
        user_input = int(input("Choose your faith! " + "\n"))
        print('\033c')
        try:
            if user_input == "" or user_input > len(menu.items):
                raise ValueError
        except:
            print("Hey, that\'s not an option!")
        return user_input

    def print_and_choose_menu_input(self):
        self.printMenu()
        self.choose(self.user_input())

class Character():
    def __init__(self, name = None, dexterity = 0, hp = 0, luck = 0, potion = None):
        self.name = name
        self.dexterity = dexterity
        self.hp = hp
        self.luck = luck
        self.potion = potion

    def input_name(self):
        print('\033c')
        self.name = input("Tell me your name, young hero! " + "\n")
        return self.name

    def dexterity_rollstat(self):
        self.dexterity = randint(1, 6) + 6
        return(print("dexterity points: " , self.dexterity))

    def health_rollstat(self):
        self.hp = randint(2, 12) + 12
        return(print("health points: " , self.hp))

    def luck_rollstat(self):
        self.luck = randint(1, 6) + 6
        return(print("luck points: " , self.luck, "\n"))

    def roll_dex_hp_luck_stats(self):
        text = input("Press Enter to roll the dice for the basic stats (dexterity, hp, luck)! " + "\n")
        self.dexterity_rollstat()
        self.health_rollstat()
        self.luck_rollstat()
        roll_stats()

    def choose_potion(self, potion):
        potion_menu(potion)

    def print_character_stat(self):
        print(self.name + " " + "stats: " + "\n")
        print("Dexterity points: ", self.dexterity)
        print("Health points: ", self.hp)
        print("Luck points: ", self.luck)

class Opponent():
    def __init__(self, name = "Sanyi", hp = 0, dexterity = 0):
        self.name = name
        self.hp = hp
        self.dexterity = dexterity

    def opp_dexterity_rollstat(self):
        self.dexterity = randint(1, 6)
        return("dexterity points: " , self.dexterity)

    def opp_health_rollstat(self):
        self.hp = randint(2, 12)
        return("health points: " , self.hp)

    def print_opp_stat(self):
        self.opp_dexterity_rollstat()
        self.opp_health_rollstat()
        print(self.name + " " + "stats: " + "\n")
        print("Dexterity points: ", self.dexterity)
        print("Health points: ", self.hp)

    def print_opp_and_char_stats(self):
        print("Test your Sword in a test fight! " + "\n")
        print(new_player.print_character_stat(), "\n")
        print(self.print_opp_stat(), "\n")
        strike_menu()

class Fight():
    def __init__(self, character_strike = None, opponent_strike = None):
        self.character_strike = character_strike
        self.opponent_strike = opponent_strike

    def current_dex(self):
        strike_dex_char = randint(2, 12)
        strike_dex_opp = randint(2, 12)
        self.character_strike = (new_player.dexterity + strike_dex_char)
        self.opponent_strike = (enemy.dexterity + strike_dex_opp)
        print(new_player.name, "dexterity during the strike" , self.character_strike)
        print(enemy.name, "dexterity during the strike" , self.opponent_strike, "\n")

    def after_strike(self):
        if self.character_strike > self.opponent_strike:
            enemy.hp -= 2
            print("OMG, you hit the f*cking MONSTER!!" , "\n" , "It has only" , enemy.hp , "hp points left")
        else:
            new_player.hp -= 2
            print("Sorry buddy, the f*cking Monster hit you!""\n" , "You have" , new_player.hp , "hp points left")

    def is_alive(self):
        if new_player.hp <= 0:
            print("You\'re dead. I think this whole hero stuff is not your thing...Or you can start again and try not to be a bitch!")
        elif enemy.hp <= 0:
            print("YOU\'VE JUST KILLED THE BEAST! F*cking amazing! I think your job is done here.")
        else:
            pass

    def strike(self):
        self.current_dex()
        self.after_strike()
        print("\n")
        self.is_alive()
        after_strike_menu()

    def try_luck(self):
        random_luck = randint(2, 12)
        if new_player.luck < random_luck and self.character_strike < self.opponent_strike:
            new_player.hp -= 3
            print("You have no luck, you have lost 3 healt points")
            strike_menu()
        elif new_player.luck >= random_luck and self.character_strike < self.opponent_strike:
            new_player.hp -= 1
            new_player.luck -= 1
            print("You are lucky")
            strike_menu()
        elif new_player.luck < random_luck and self.character_strike > self.opponent_strike:
            new_player.hp -= 1
            print("You have no luck")
            strike_menu()
        elif new_player.luck >= random_luck and self.character_strike > self.opponent_strike:
            new_player.hp -= 4
            new_player.luck -= 1
            print("This is luck!")
            strike_menu()

def exit_game():
    pass

def after_strike_menu():
    after_strike_menu = Menu([
                MenuItem(1, "Continue", fight.strike),
                MenuItem(2, "Try your luck", fight.try_luck),
                MenuItem(3, "Retreat", None),
                MenuItem(4, "Quit", quit_game)
                ])
    after_strike_menu.print_and_choose_menu_input()

def strike_menu():
    strike_menu = Menu([
                MenuItem(1, "Strike", fight.strike),
                MenuItem(2, "Retreat", None),
                MenuItem(3, "Quit", quit_game)
                ])
    strike_menu.print_and_choose_menu_input()

def begin_game_menu():
    begin_game_menu = Menu([
                MenuItem(1, "Begin", None),
                MenuItem(2, "Save", None),
                MenuItem(3, "Quit", quit_game)
                ])
    new_player.print_character_stat()
    begin_game_menu.print_and_choose_menu_input()

def potion_chooser():
    potions = Menu([
                MenuItem(1, "Potion of Health", lambda: new_player.choose_potion("Potion of Health")),
                MenuItem(2, "Potion of Dexterity", lambda: new_player.choose_potion("Potion of Dexterity")),
                MenuItem(3, "Potion of Luck", lambda: new_player.choose_potion("Potion of Luck"))
                ])
    potions.print_and_choose_menu_input()

def potion_menu(potion):
    print("Your selected potion is: " + potion + "\n")
    potion_menu = Menu([
                MenuItem(1, "Reselect the Potion", potion_chooser),
                MenuItem(2, "Continue", enemy.print_opp_and_char_stats),
                MenuItem(3, "Quit", quit_game)
                ])
    potion_menu.print_and_choose_menu_input()

def roll_stats():
    roll_stats_menu_items = Menu([
                MenuItem(1, "Re-roll stats", new_player.roll_dex_hp_luck_stats),
                MenuItem(2, "Continue", potion_chooser),
                MenuItem(3, "Save", None),
                MenuItem(4, "Quit", quit_game)
                ])
    roll_stats_menu_items.print_and_choose_menu_input()

def quit_game():
    quit_game_menu_items = Menu([
                MenuItem(1, "Save and Quit", exit_game),
                MenuItem(2, "Quit without save", exit_game),
                MenuItem(3, "Resume", new_game_action)
                ])
    quit_game_menu_items.print_and_choose_menu_input()

def new_game_action():
    new_game_name_items = Menu([
                MenuItem(1, "Re-enter name", new_player.input_name),
                MenuItem(2, "Continue", new_player.roll_dex_hp_luck_stats),
                MenuItem(3, "Save", None),
                MenuItem(4, "Quit", quit_game)
                ])
    new_player.input_name()
    new_game_name_items.print_and_choose_menu_input()

menu_items = [
          MenuItem(1, 'New Game', new_game_action),
          MenuItem(2, 'Load Game', None),
          MenuItem(3, 'Exit Game', quit_game)
        ]

menu = Menu(menu_items)
new_player = Character()
enemy = Opponent()
fight = Fight()
menu.print_and_choose_menu_input()
