def drop_off():
    name1 = input("What is the name of the child you are dropping off? ")

    while len(name1) < 3:
        name1 = input("please enter valid name: ")
    roll.append(name1)
    print()
    print(name1, "was added to roll.")
    print()


def pick_up():
    name2 = input("What is the name of the child ou are picking up? ")
    if name2 in roll:
        roll.remove(name2)
        print(name2,"was removed from the roll.")
        print()
    else:
        print("There's no",name2,"here at present. Please check name.")
        print()

def calc_cost(number):
    rate=12.00
    hours=int(input("How many hours to change for: "))
    cost=number * hours * rate
    return cost

def print_roll():
    print("MGS Daycare clients currently presents are: ")
    for item in roll:
        print(f"\t{item}")
    print()


choice = 0
roll = []
while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        drop_off()
    elif choice == 2:
        pick_up()

    elif choice == 3:
        print(f"The charge for looking after{len(roll)} children is "
              f"${calc_cost(len(roll)):.2f}")
    elif choice == 4:
        print_roll()

    elif choice == 5:
        print("Goodbye")

    else:
        print("enter the number between 1 to 5")






