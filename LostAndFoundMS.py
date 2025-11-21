#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dictionary for storing users & admin login details
users = {
    "admin": {"password":"admin123","role":"admin"}
}

lostItem = []
foundItem = []

#add lost item
def addLostItem():
    print("\n--- Add Lost Item ---")
    name = input("Enter Your Name: ")
    itemName = input("Enter the Lost Item Name: ")
    color = input ("Enter the color of Item: ")
    location = input("Enter the location where item lost: ")
    date = input("Enter the date (dd-mm-yy): ")

    item = {
        "name":name,
        "itemName":itemName,
        "color" :color,
        "location":location,
        "date":date,
        "status":"lost"
    }

    lostItem.append(item)
    print(f"lost Item {itemName} added in Record Successfully.")


#add found item
def addFoundItem():
    print("\n--- Add Found Item ---")
    name = input("Enter Your Name: ")
    itemName = input("Enter the Found Item Name: ")
    color = input ("Enter the color of Item: ")
    location = input("Enter the location where item Found: ")
    date = input("Enter the date (dd-mm-yy): ")

    item = {
        "name":name,
        "itemName":itemName,
        "color" :color,
        "location":location,
        "date":date,
        "status":"found"
    }

    foundItem.append(item)
    print(f"Found Item {itemName} added in Record Successfully.")


def viewItemList(itemList, title):
    print(f"\n--- {title} ---")
    if not itemList:
        print("No items to show.")
        return
    for idx, item in enumerate(itemList, 1):
        print(f"{idx}. {item['itemName']} | Owner: {item['name']} | Color: {item['color']} | Location: {item['location']} | Date: {item['date']} | Status: {item['status']}")


def searchMatches():
    print("\n--- Search Matches ---")
    foundMatch = False
    for lost in lostItem:
        for found in foundItem:
            if (lost["itemName"].lower() == found["itemName"].lower() and
                lost["color"].lower() == found["color"].lower()):
                print(f"Match found: {lost['itemName']} (Lost by {lost['name']}) and (Found by {found['name']})")
                foundMatch = True
    if not foundMatch:
        print("No matches found.")


def markReturned():
    print("\n--- Mark Item as Returned ---")
    viewItemList(lostItem, "Lost Items")
    idx = int(input("Enter number of the lost item to mark returned: "))
    if 1 <= idx <= len(lostItem):
        lostItem[idx-1]["status"] = "Returned"
        print("Item marked as Returned")
    else:
        print("Invalid Selection.")


def deleteItem(role):
    print("\n Delete Item ")
    viewItemList(lostItem, "Lost Items")
    viewItemList(foundItem, "Found Items")
    choice = input("Delete from (lost/found): ").lower()
    if choice == "lost":
        lst = lostItem
    elif choice == "found":
        lst = foundItem
    else:
        print("Invalid choice")
        return
    idx = int(input("Enter item number to delete: "))
    if 1 <= idx <= len(lst):
        removed = lst.pop(idx-1)
        print(f"Item '{removed['itemName']}' deleted successfully.")
    else:
        print("Invalid selection.")

def summary():
    totalLost = len(lostItem)
    totalFound = len(foundItem)
    returned = sum(1 for item in lostItem if item["status"]=="Returned")
    matches = 0
    for lost in lostItem:
        for found in foundItem:
            if lost["itemName"].lower() == found["itemName"].lower() and lost["color"].lower() == found["color"].lower():
                matches += 1
    print("\n Summary")
    print(f"Total Lost Items: {totalLost}")
    print(f"Total Found Items: {totalFound}")
    print(f"Total Matches: {matches}")
    print(f"Total Returned: {returned}")


def register():
    print("\n--- Register New User ---")
    username = input("Enter  username: ")
    if username in users:
        print("Username already exists!")
        return
    password = input("Enter a password: ")
    users[username] = {"password": password, "role": "user"}
    print("User Added Successfully")

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        print(f"Login Successfull. Welcome {username}")
        return users[username]["role"]
    else:
        print("Login was not successfull.")
        return None

def main():
    print("\n--- Lost and Found Management System --- ")
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter Your Choice: ")
        if choice =="1":
            register()
        elif choice =="2":
            role = login()
            if role:
                while True:
                    print("\n ---Menu---")
                    print("1. Add Lost Item")
                    print("2. Add Found Item")
                    print("3. View Lost Items")
                    print("4. View Found Items")
                    print("5. Search Matches")
                    print("6. Mark Lost Item as Returned")
                    if role=="admin":
                        print("7. Delete Item")
                    print("8. Summary")
                    print("9. Logout")
                    option = input("Enter Your option: ")
                    if option=="1":
                        addLostItem()
                    elif option=="2":
                        addFoundItem()
                    elif option=="3":
                        viewItemList(lostItem, "Lost Items")
                    elif option=="4":
                        viewItemList(foundItem, "Found Items")
                    elif option=="5":
                        searchMatches()
                    elif option=="6":
                        markReturned()
                    elif option=="7" and role=="admin":
                        deleteItem(role)
                    elif option=="8":
                        summary()
                    elif option=="9":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option.")
        elif choice=="3":
            print("Exiting system...")
            break
        else:
            print("Invalid option.")

#run progrm
main()


# In[ ]:




