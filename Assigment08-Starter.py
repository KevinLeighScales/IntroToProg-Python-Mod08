# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Kevin Scales, 3.7.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kevin Scales, 3.7.2021,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price

    def info(self):
        return(self.product_name, self.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kevin Scales,3.7.2021,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    @staticmethod
    def ReadFileDataToString(file_name: str, lstOfProductObjects):
        """ reads data from file"""
#        lstOfProductObjects = []
        try:
            f = open(file_name, 'r')
            for line in f:
                name, price = line.split(",")
                row = {"name": name.strip(), "price": price.strip()}
                lstOfProductObjects.append(row)
            f.close()
        except Exception as e:
            print("A general error occured.")
            print(e, e.__doc__, type(e), sep='\n')
        return lstOfProductObjects

    # TODO: Add Code to process data to a file
    @staticmethod
    def WriteDataToFile(file_name, lstOfProductObjects):
        """ save data to file
        :param file_name:
        :param list_objects:
        :return:
        """
        success_status = False
        try:
            f=open(file_name, 'w')
            for row in lstOfProductObjects:
                f.write(row["name"] + ', ' + row["price"] + '\n')
            f.close()
            success_status = True
        except Exception as e:
            print("A general error occured.")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO(object):
    # TODO: Add docstring
    """ Handle the input and display (output)

    methods:
        DisplayMedu
        GetChoice
        DisplayData
        AddData
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Save Data to File        
        3) Exit Program (w/o save)
        ''')
    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_data(lstOfProductObjects):

        """ Displays data"""
        for row in lstOfProductObjects:
            print(row["name"] + " (" + row["price"] + ")")

#            print(FileProcessor.ReadFileDataToString(lstOfProductObjects))

    # TODO: Add code to get product data from user
    @staticmethod
    def input_data():
        item = str(input("Item name:  ")).strip()
        price = str(input("Item price: ")).strip()
        return item, price

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
f = FileProcessor()
lstOfProductObjects = f.ReadFileDataToString(strFileName,lstOfProductObjects)
IO.show_data(lstOfProductObjects)  # Show current data in the list/table

while(True):
    IO.print_menu_Products()
    choice = IO.input_menu_choice()
    if str(choice) == "1":
        name, price = IO.input_data()
        row = {"name": name, "price": price}
        lstOfProductObjects.append(row)
        IO.show_data(lstOfProductObjects)
        continue  # to show the menu
    elif str(choice) == "2":
        f.WriteDataToFile(strFileName,lstOfProductObjects)
    elif str(choice) == "3":
        print("Goodbye!")
        break  # and Exit
