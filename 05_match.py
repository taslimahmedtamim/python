# match is similar to switch-case in other languages
# break statements are not needed in python match-case

x = input("Enter a number:")
match x:
    case 1:
        print("saturday")
    case 2:
        print("sunday")
    case 3:
        print("monday")
    case 4:
        print("tuesday")
    case 5:
        print("wednesday")
    case 6:
        print("thursday")
    case 7:
        print("friday")
    case _:
        print("invalid input")
        