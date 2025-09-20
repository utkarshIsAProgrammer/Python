day = int(input("Enter day number: "))

match day:
    case 1:
        print("It's monday")
    case 2:
        print("It's Tuesday")
    case 3:
        print("It's Wednesday")
    case 4:
        print("It's Thursday")
    case 5:
        print("It's Friday")
    case 6:
        print("It's Saturday")
    case 7:
        print("It's Sunday")
    case _:
        print("Looking forward in this week!")

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Week day!")
    case 6 | 7:
        print("Weekend day!")
    case _:
        print("Looking forward in this week!")
