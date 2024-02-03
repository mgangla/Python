#Create a simple inventory management system. 

#function to open a csv file
#import csv library

import csv


#Create a menu to get the user input
#user has 4 options (add,remove,update,display)
def menu():

    print("===== Welcome to a Simple Inventory System =====")
    while True:
        choice = input("Enter an option \n 1- for add item\n 2 for Remove Stock item \n 3 For update stock \n 4 for display Stock \n")
        if '1' in choice:
         (Item.add_item)
        elif '2' in choice:
             (Item.remove_item)
        elif '3' in choice:
             (Item.update_item)
        elif '4' in choice:
             (Item.display_item)
        else :
            print("Please enter a valid choice.")
            print("\n")



#defn class inventory

 
class Item :
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity= quantity 
        self.price = price
    
    #defn class Inventory System 
class Inventory_System :
    def __init__(self):
        self.inventory = []

    def add_item(self,Item):
        
        name =input ("enter the item name")
        quantity= int(input ("enter the stock quantity"))
        price = float(input ("enter the price for the item"))
        self.inventory.append(Item)

        print (f"{name}{quantity}{price} have been added to the inventory")
       # return (add_item)
    
    def remove_item(self,Item) :
        name = ("enter the item name")
        quantity = ("enter the quantity to remove")
        if name in inventory:
            if inventory[name]>= quantity:
                if inventory[name]<=quantity:
                    if inventory[name] ==0:
                        del inventory[name]
                else:
                    print("not enough item in the inventory")
        else :
            print("item not found")

        #def  update_item(self) :
         
         #return
    
    def display_item(self):
        print(" this is the current stock items")

        for item in inventory:
          
            print(f"name:{item.name},quantity :{item.quantity},price :{item.price}"
                  )
    print(display_item)

inventory = Inventory_System () #call inventory class
#store data in a csv
with open("inventory.csv","w",newline= '')as csvfile :
    writer=csv.writer(csvfile)
    writer.writerow(inventory())

    for inventory in Inventory_System :
       writer.writerow([inventory])

