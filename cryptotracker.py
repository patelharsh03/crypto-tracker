from handlers import add_new_crypto, view_all_crypto, update_crypto, delete_crypto

def main():
    while True:
        print('''******** Crypto Manager *********
    Select an option:
    1. Add a new crypto
    2. View all crypto 
    3. Update a crypto 
    4. Delete a crypto
    5. Exit \n''')
        
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                add_new_crypto()
            case 2:
                view_all_crypto()
            case 3:
                update_crypto()
            case 4:
                delete_crypto()
            case 5:
                print("Exiting...")
                break
            case _:
                print("Invalid choice")
                exit(1)
            
if __name__ == "__main__":
    main()