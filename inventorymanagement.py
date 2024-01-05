import pandas as pd 
import datetime as datetime 

class InventoryManagement:
    def __init__(self):
        self.item = pd.DataFrame(columns=["Item Name", "Item Id", "Quantity", "Adding Date"])

    def add_item(self):
        item__name = input("Enter the item name: ")
        item_id = int(input("Enter item id: "))
        quantity = int(input("Enter quantity: "))
        adding_date = datetime.datetime.now()
        new_item = pd.DataFrame([[item__name, item_id, quantity, adding_date]],
                                columns=["Item Name", "Item Id", "Quantity", "Adding Date"])
        self.item = pd.concat([self.item, new_item], ignore_index=True)
        print("Item added Successfully")


    def view_item(self):
        if self.item.empty:
            print("No items available")
        else:
            print(self.item)
        

    def update_item(self):
        item_id = int(input("Enter item id to update: "))
        if item_id>=len(self.item):
            print("Item not found")
        else:
            print("Update item id: ", item_id)
            self.item.at[item_id, "Item"] = input("Enter new item: ")
            self.item.at[item_id, "Quantity"] = int(input("Enter new quantity: "))
            print("Item Updated Successfully.")

    def save_to_excel(self):
        self.item.to_excel("inventorymanagement.xlsx", index = False)
        print("Item saved to 'inventorymanagement.xlsx'.")

order_system = InventoryManagement()

while True:

    print("\n1. Add item\n2. View item\n3. Update item\n4. Save to excel\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        order_system.add_item()
        #enter item id in sequence
    elif choice == "2":
        order_system.view_item()
    elif choice == "3":
        order_system.update_item()
    elif choice == "4":
        order_system.save_to_excel()
    elif choice == "5":
        break 
    else:
        print("Invalid choice. Please try again.")
