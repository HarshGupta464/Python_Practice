while True:
    name = input("Enter customer's name: ")
    Total=0
    while True:
        amount = float(input("Enter the amount: "))
        quantity = int(input("Enter the quantity: "))
        Total += amount * quantity
        repeat= input("Do you want to enter more items? (y/n)" )
        if repeat == "n":
            break
    print("-" * 50)
    print("Name: ", name)
    print("Total =", Total)
    print("-" * 50)
    cust_rep=input("Do you want to add more customer?(y/n) ")
    if cust_rep == "n":
        break

