import funcs
import help

help_menu = help.help()

run = True

while run:
    cmd = input("$> ")

    match cmd:
        case "help":
            print("For help please go to ")