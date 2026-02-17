import json
from pathlib import Path


class InventoryManager:
    database="data.json"
    data=[]
    try:
        if Path(database).exists():
            with open(database,'r') as f:
                data=json.load(f)
        else:
            print("No such file exists")
    except Exception as err:
        print(f'error is {err}')
        
    @staticmethod
    def update():
        with open(InventoryManager.database, 'w') as f:
            f.write(json.dumps(InventoryManager.data, indent=4))
                
    def check_duplicate(self, name):
        for item in InventoryManager.data:
            if item["name"].lower() == name.lower():
                return item
        return None
    def add_item(self):
        name = input("Enter the name of the item: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        print("Select category:")
        print("1. Electronics")
        print("2. Clothing")
        print("3. Food")
        print("4. Books")
        print("5. Grocery")
        category_choice = int(input("Enter your choice: "))

        categories = {
            1: "Electronics",
            2: "Clothing",
            3: "Food",
            4: "Books",
            5: "Grocery"
        }

        if category_choice in categories:
            category = categories[category_choice]
        else:
            print("Invalid choice. Defaulting to 'Other'.")
            category = "Other"


        existing_item = self.check_duplicate(name)

        if existing_item:
            existing_item["quantity"] += quantity
            print("Item already exists. Quantity updated successfully!")
        else:
            item = {
                "name": name,
                "quantity": quantity,
                "price": price,
                "category": category,
            }
            InventoryManager.data.append(item)
            print("Item added successfully!")

        InventoryManager.update()
    def view_items(self):
        if not InventoryManager.data:
            print("No item found in inventory")
        else:
            print("Items in inventory:")
            for item in InventoryManager.data:
                print(f'Name: {item["name"]}, Quantity: {item["quantity"]}, Price: {item["price"]}, Category: {item["category"]}')

            
    def update_item(self):
        name=input('Enter the name of the item you want to update: ')
        for item in InventoryManager.data:
            if item['name'].lower()==name.lower():
                item['quantity']=int(input('Enter the new quantity: '))
                item['price']=float(input('Enter the new price: '))
                print("Select category:")
                print("1. Electronics")
                print("2. Clothing")
                print("3. Food")
                print("4. Books")
                print("5. Grocery")
                category_choice = int(input("Enter your choice: "))

                categories = {
                    1: "Electronics",
                    2: "Clothing",
                    3: "Food",
                    4: "Books",
                    5: "Grocery"
                }

                if category_choice in categories:
                    item['category'] = categories[category_choice]
                else:
                    print("Invalid choice. Defaulting to 'Other'.")
                    item['category'] = "Other"
                InventoryManager.update()
                print("Item updated successfully")
                

    def delete_item(self):
        name=input('Enter the name of the item you want to delete: ')
        for item in InventoryManager.data:
            if item['name'].lower()==name.lower():
                InventoryManager.data.remove(item)
                InventoryManager.update()
                print("Item deleted successfully")

manager=InventoryManager()  
while True:

    print("Welcome to Inventory Manager")
    print("Press 1 to add an item")
    print("Press 2 to view all items")
    print("Press 3 to update an item")
    print("Press 4 to delete an item")
    print("Press 5 to exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        manager.add_item()
    elif choice==2:
        manager.view_items()
    elif choice==3:
        manager.update_item()
    elif choice==4:
        manager.delete_item()    
    elif choice==5:
        print("Exiting Inventory Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    



























