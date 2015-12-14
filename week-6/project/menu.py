

menu_items = [{"name": "New Game"},
              {"name": "Load Game"},
              {"name": "Exit"}]

new_game_items = [{"name": "Re-enter name"},
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
                new_game_menu = NewGame(new_game_items)
                new_game_menu.menuChooser()
            elif chooser == 2:
                pass
            elif chooser == 3:
                self.exitGame()
        except:
            print("Hey, that\'s not an option!")

    def exitGame(self):
        pass

menu = Menu(menu_items)
menu.menuChooser()

class NewGame(Menu):
    def __init__(self, new_game_items):
        self.new_game_items = new_game_items

    def menuChooser(self):
        print("asvd")

menu = NewGame(new_game_items)
menu.menuChooser()
