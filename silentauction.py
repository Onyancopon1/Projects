"""Program to run a silent auction
"""


def check_input(question):
    error = "That was not a valid number"
    while True:
        try:
            number=float(input(question))
            return number
        except ValueError:
            print(error)


def welcome(text,symbol):
    print(symbol*len(text))
    print(text)
    print(symbol*len(text))
    print()


#main routine
bid=0.0
highest=0.0
welcome("Koei best auctions","*")
item=input("What is the auctions for")
reserve=check_input("What is the reserve price? $")
print()
print("The auction for the ",item,"has started!")

while bid !=-1:
    print(f"\nThe highest bid so is${highest:.2f}")
    bid=check_input("What is your bid?(-1 to quit) $ ")