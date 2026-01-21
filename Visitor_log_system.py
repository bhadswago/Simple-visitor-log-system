visitors = []

def add_visitor():
    name = input("Enter visitor name: ")
    purpose = input("Enter visit purpose: ")
    visitors.append({"name": name, "purpose": purpose})
    print("Visitor logged")

def view_visitors():
    if not visitors:
        print("No visitors recorded")
    else:
        for visitor in visitors:
            print(visitor["name"], "-", visitor["purpose"])

def main():
    while True:
        print("1. Add Visitor")
        print("2. View Visitors")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_visitor()
        elif choice == "2":
            view_visitors()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
