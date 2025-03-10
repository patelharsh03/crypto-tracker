import json
from prettytable import PrettyTable

file_name = "crypto.json"

def data_save_helper(crypto):
    with open(file_name, "w") as file:
        json.dump(crypto, file)

def load_crypto():
    try:
        with open(file_name, "r") as file:
            crypto = json.load(file)
            return crypto
    except FileNotFoundError:
        return []

crypto = load_crypto()

def add_new_crypto():
    name = input("Enter the name of the crypto: ")
    buying_price = float(input("Enter the buying price: "))
    quantity = float(input("Enter the quantity: "))
    crypto.append({
        "name": name,
        "buying_price": buying_price,
        "quantity": quantity
    })
    data_save_helper(crypto)
    

def view_all_crypto():
    print ("\n#*#*#*#*#* Your portfolio #*#*#*#*#*\n")
    table = PrettyTable(["Sr no.", "Crypto Name", "Buying Price($)", "Quantity"])
    for index, cry in enumerate(crypto, start=1):
        table.add_row([index, cry["name"], cry["buying_price"], cry["quantity"]])
    print(table)
    print ("\n")
    
def update_crypto():
    view_all_crypto()
    index = int(input("Enter the index of the crypto you want to update: "))
    cry = crypto[index - 1]
    print("Enter the new details, press enter if you don't want to update: ")
    name = input(f"Enter the name of the crypto (Current name: {cry["name"]}): ")
    buying_price = input(f"Enter the buying price (Current price: {cry["buying_price"]}): ")
    quantity = input(f"Enter the quantity (Current quantity {cry["quantity"]}): ")
    crypto[index - 1] = {
        "name": name if name else cry["name"],
        "buying_price": float(buying_price) if buying_price else cry["buying_price"],
        "quantity": float(quantity) if quantity else cry["quantity"]
    }
    data_save_helper(crypto)

def delete_crypto():
    view_all_crypto()
    index = int(input("Enter the index of the crypto you want to delete: "))
    del crypto[index - 1]
    data_save_helper(crypto)
