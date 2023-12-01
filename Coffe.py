avlqty = {"Water": 2000, "Coffee powder": 100, "Milk": 1000}
espresso = {"Water": 50, "Coffee powder": 18, "Milk": 0, "Price": 15}
Latte = {"Water": 200, "Coffee powder": 24, "Milk": 150, "Price": 25}
Cappuccino = {"Water": 250, "Coffee powder": 24, "Milk": 100, "Price": 30}
valofmoneyins = 0
sales_e = 0
sales_l = 0
sales_c = 0
sales = 0
print("Sairam!")
print()

while True:
    print("Enter 1 for Espresso\nEnter 4 for Latte\nEnter 9 for Cappuccino")
    want = str(int(input("Choose the coffee you want:")))
    if want == 1:
        print("The price of espresso is: ", espresso["Price"], "/-", sep="")
        print("Please insert the coins in the correct box!")
        ten = int(input("Enter the number of ten rupee coins inserted:"))
        valofmoneyins += ten * 10
        five = int(input("Enter the number of five rupee coins inserted:"))
        valofmoneyins += five * 5
        two = int(input("Enter the number of two rupee coins inserted:"))
        valofmoneyins += two * 2
        one = int(input("Enter the number of one rupee coins inserted:"))
        valofmoneyins += one
        print(f"Sum total of money inserted is: {valofmoneyins}/-")
        if valofmoneyins < espresso["Price"]:
            valofmoneyins
            print("Money is not sufficient")
        elif valofmoneyins > espresso["Price"]:
            change = valofmoneyins - espresso["Price"]
            print("Here is your change: ", change, "/-")
            print("Please collect your coffee")
        else:
            print("Here is your coffee")
        avlqty["Water"] -= espresso["Water"]
        avlqty["Coffee powder"] -= espresso["Coffee powder"]
        avlqty["Milk"] -= espresso["Milk"]
        sales_e += 1
        sales += espresso["Price"]
    elif want == 4:
        print("The price of latte is:", Latte["Price"], "/-")
        print("Please insert the coins in the correct box!")
        ten = int(input("Enter the number of ten rupee coins inserted:"))
        valofmoneyins += ten * 10
        five = int(input("Enter the number of five rupee coins inserted:"))
        valofmoneyins += five * 5
        two = int(input("Enter the number of two rupee coins inserted:"))
        valofmoneyins += two * 2
        one = int(input("Enter the number of one rupee coins inserted:"))
        valofmoneyins += one
        print(f"Sum total of money inserted is: {valofmoneyins}/-")
        if valofmoneyins < Latte["Price"]:
            print("Money is not sufficient")
            ret = 0
            print("Please collect your money back", valofmoneyins)
        elif valofmoneyins > Latte["Price"]:
            change = valofmoneyins - Latte["Price"]
            print("Here is your change: ", change, "/-")
            print("Please collect your coffee")


        elif print("Here is your coffee"):
            sales += Latte["Price"]
        avlqty["Water"] -= Latte["Water"]
        avlqty["Coffee powder"] -= Latte["Coffee powder"]
        avlqty["Milk"] -= Latte["Milk"]
        sales_l += 1
        sales += Latte["Price"]
    elif want == 9:
        print("The price of cappuccino is:", Cappuccino["Price"], "/-")
        print("Please insert the coins in the correct box!")
        ten = int(input("Enter the number of ten rupee coins inserted:"))
        valofmoneyins += ten * 10
        five = int(input("Enter the number of five rupee coins inserted:"))
        valofmoneyins += five * 5
        two = int(input("Enter the number of two rupee coins inserted:"))
        valofmoneyins += two * 2
        one = int(input("Enter the number of one rupee coins inserted:"))
        valofmoneyins += one
        print(f"Sum total of money inserted is: {valofmoneyins}/-")
        if valofmoneyins < Cappuccino["Price"]:
            print("Money is not sufficient")
        elif valofmoneyins > Cappuccino["Price"]:
            change = valofmoneyins - Cappuccino["Price"]
            print("Here is your change: ", change, "/-")
            print("Please collect your coffee")
        else:
            print("Here is your coffee")
        avlqty["Water"] -= Cappuccino["Water"]
        avlqty["Coffee powder"] -= Cappuccino["Coffee powder"]
        avlqty["Milk"] -= Cappuccino["Milk"]
        sales_c += 1
        sales += Cappuccino["Price"]
    else:
        print("Choose the correct number")
    any = int(input("Enter 9 to purchase more:"))
    if (any == 9):
        valofmoneyins = 0
        continue
    else:
        print("Operator login")
        cont = int(input("Press 1 to continue:"))
        if cont == 1:
            pwd = int(input("Enter password:"))
            if pwd == 4455:
                inp = int(input(
                    "If you want to check the revenue enter 1\nIf you want to check the sales of products enter 2 \n if you want to check inventory enter any other key:"))
                if (inp == 1):
                    print("The total revenue today is", sales, "/-")

                elif inp == 2:
                    print("The total sales of espresso are:", sales_e)
                    print("The total sales of Latte are:", sales_l)
                    print("The total sales of Cappuccino are:", sales_c)
                else:
                    print("The left over quantity is:", avlqty)

            else:
                print("Incorrect password!")
                break

