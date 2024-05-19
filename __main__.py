import funcs
import help

help_menu = help.help()

run = True

while run:
    cmd = input("$> ")

    match cmd:
        case "help":
            while True:
                specify = input("What would documentation would you like to see specificly. (Type all to veiw all and type nothing to go back.) ").lower()
                if specify == "all":
                    print(" ".join(help_menu))
                    break
                elif specify == "":
                    break
                else:
                    try:
                        print(help_menu[specify])
                        break
                    except:
                        print("There is no section on that. Please try again")
                        continue