import datetime
import time
import csv


def bring_menu():
    # Open the file in write mode and write the menu
    with open("Menu.txt", "w", encoding="utf-8") as menu:
        menu.write("""
                * Please Choose a Pizza Base: 
                1: Classic 
                2: Margherita 
                3: TurkPizza 
                4: PlainPizza 

                * and sauce of your choice: 
                11: Olives 
                12: Mushrooms 
                13: GoatCheese 
                14: Meat 
                15: Onions 
                16: Corn 
                * Thank you!
        """)
    # Open the file in read mode and print the menu
    with open("Menu.txt", "r", encoding="utf-8") as menu:
        print(menu.read())


class Pizza():  # Base Pizza class
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Types of pizza
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Garnished with tomatoes, basil and mozzarella cheese, in order to represent the Italian flag",
                         50)


class MargeritaPizza(Pizza):
    def __init__(self):
        super().__init__("Red tomato sauce, white mozzarella and fresh green basil", 60)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__(
            "Made of unleavened dough topped with ground lamb or beef, garlic, spices, and other ingredients", 70)


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("No toppings at all , an unadorned flatbread simply seasoned with salt and olive oil.", 75)


class Sauce():  # Base Sauce class
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description


# Types of sauce
class Olives(Sauce):
    def __init__(self):
        super().__init__(5, "Olives")


class Mushrooms(Sauce):
    def __init__(self):
        super().__init__(5, "Mushrooms")


class GoatCheese(Sauce):
    def __init__(self):
        super().__init__(5, "GoatCheese")


class Meat(Sauce):
    def __init__(self):
        super().__init__(5, "Meat")


class Onions(Sauce):
    def __init__(self):
        super().__init__(5, "Onions")


class Corn(Sauce):
    def __init__(self):
        super().__init__(5, "Corn")


def select_pizza():
    pizza_choice = input("Select Pizza (1-4) : ")
    if pizza_choice == "1":
        pizza = ClassicPizza()
        return pizza.get_description() + " " + str(pizza.get_cost()) + " TL"
    elif pizza_choice == "2":
        pizza = MargeritaPizza()
        return pizza.get_description() + " " + str(pizza.get_cost()) + " TL"
    elif pizza_choice == "3":
        pizza = TurkPizza()
        return pizza.get_description() + " " + str(pizza.get_cost()) + " TL"
    elif pizza_choice == "4":
        pizza = PlainPizza()
        return pizza.get_description() + " " + str(pizza.get_cost()) + " TL"
    else:
        print("Please enter a valid value.")


def select_sauce():
    sauce_choice = input("Select Sauce (11-16) : ")
    if sauce_choice == "11":
        sauce = Olives()
        return sauce.get_description() + " " + str(sauce.get_cost()) + " TL"
    elif sauce_choice == "12":
        sauce = Mushrooms()
        return sauce.get_description() + " " + str(sauce.get_cost()) + " TL"
    elif sauce_choice == "13":
        sauce = GoatCheese()
        return sauce.get_description() + " " + str(sauce.get_cost()) + " TL"
    elif sauce_choice == "14":
        sauce = Meat()
        return sauce.get_description() + " " + str(sauce.get_cost()) + " TL"
    elif sauce_choice == "15":
        sauce = Onions()
        return sauce.get_description() + " " + str(sauce.get_cost()) + " TL"
    elif sauce_choice == "16":
        sauce = Corn()
        return sauce.get_description() + " " + str(sauce.get_cost()) + " TL"
    else:
        print("Please enter a valid value.")


def summary():
    print("Selected Pizza : {}\nSelected Sauce : {}\n".format(select_pizza(), select_sauce()))
    print("-----------------------------------------")


class Order:
    def __init__(self):
        self.isim = None
        self.kart_numarasi = None
        self.kart_sifresi = None
        self.adres = None

    def get_payment(self):
        self.isim = input("Name surname: ")
        self.kart_numarasi = input("Credit Card Number: ")
        self.kart_sifresi = input("Credit card password: ")
        self.adres = input("Delivery address : ")

        print("Checking card information...")
        time.sleep(3)
        print("Your order has been confirmed. Enjoy your meal. :)")
        print("\n")

    def slip(self):
        # Automatically generated order date and time
        siparis_tarihi = datetime.datetime.now()

        print("*****Order Information*****")
        data = print(
            "Name : {}\tCardNo : {}\tCarsPass : ****\tAdres : {}\tDate : {}\t"
            .format(self.isim,self.kart_numarasi,self.adres,siparis_tarihi.strftime( "%d/%m/%Y  %H:%M")))

        print("\n")
        print("ORDER DATABASE")
        database = [{'Name': self.isim, 'CardNo': self.kart_numarasi, 'CardPassword': "*******", "Adres": self.adres,
                     'Date': siparis_tarihi.strftime("%d/%m/%Y  %H:%M")}]
        with open("Orders_Database.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'CardNo', 'CardPassword', 'Adres', 'Date'])
            writer.writerows(database)
            file.close()
        with open("Orders_Database.csv", "r") as f:
            menu = f.read()
            print(menu)
            f.close()


bring_menu()
print("-----------------------------------------")
summary()

order = Order()
order.get_payment()
order.slip()




