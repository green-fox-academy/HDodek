import os

filename = "list.txt"

def list_items():
    text = open("list.txt", "r").readlines()
    for index, line in enumerate(text):
        print(index +1, line)
    todo_menu()


def todo_menu():
    print("1. Current list" + "\n" + "2. Add item" + "\n" + "3. Remove item" + "\n" + "4. Move item to Complete direntory" + "\n" + "5. EXIT" + "\n")
    chooser = int(input("Choose an action!  "))
    if chooser == 1:
        list_items()
    elif chooser == 2:
        add_item()
    elif chooser == 3:
        remove_item()
    elif chooser == 4:
        move_item()
    elif chooser == 5:
        pass
    else:
        print("You can not choose that!")


def add_item():
    text = open("list.txt", "a")
    new_item = input("Give me a new TODO! ")
    text.write(new_item + "\n")
    text.close()
    todo_menu()

def remove_item():
    text = open("list.txt", "r").readlines()
    remove_item = int(input("What would you like to delete? "))
    text_write = open("list.txt", "w")
    del text[remove_item -1]
    for line in text:
        text_write.write(line)
    text_write.close()
    return todo_menu()

def move_item():
   text = open("list.txt", "r").readlines()
   move_item = int(input( "Which TODO is complete? "))
   completed_item = open("completed.txt", "w")
   completed_item.write(text[move_item - 1])
   text_write = open("list.txt", "w")
   del text[move_item -1]
   for line in text:
       text_write.write(line)
   text_write.close()
   return todo_menu()








todo_menu()
