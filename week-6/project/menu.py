


menu_items = [{"name": "New Game"},
              {"name": "Load Game"},
              {"name": "Exit"}]

new_game_name_items = [{"name": "Re-enter name"},
                       {"name": "Continue"},
                       {"name": "Save"},
                       {"name": "Quit"}]

class Menu():
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def printMenu(self):
        for index, item in enumerate(self.menu_items):
            print(index + 1, item["name"])

    def menuChooser(self):
        self.printMenu()
        try:
            chooser = int(input("Choose your faith! "))
            if chooser == "" or chooser > 3:
                raise ValueError
            elif chooser == 1:
                new_game_menu = NewGame(new_game_name_items)
                new_game_menu.userName()
            elif chooser == 2:
                pass
            elif chooser == 3:
                self.exitGame()
        except:
            print("Hey, that\'s not an option!")

    def exitGame(self):
        pass

class NewGame(Menu):
    def __init__(self, new_game_items):
        self.new_game_items = new_game_items

    def print_name_sub_menu(self):
        for index, item in enumerate(self.new_game_items):
            print(index + 1, item["name"])

    def userName(self):
        print("\033c")
        username = input("Please, give me your name young hero! " + "\n")
        print("God day" + " " + username + "!"+ " ")
        self.name_sub_chooser()

    def name_sub_chooser(self):
        self.print_name_sub_menu()
        try:
            chooser = int(input("What\'s next?"+ "\n"))
            if chooser == "" or chooser > 4:
                raise ValueError
            elif chooser == 1:
                pass
            elif chooser == 2:
                pass
            elif chooser == 3:
                self.exit_name()
        except:
            print("Hey, that\'s not an option!")

    def exit_name(self):
        menuChooser()


menu = Menu(menu_items)
menu.menuChooser()
