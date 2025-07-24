while True :
    Name=input("Enter customer's name: ")
    total =0

    while True :
        print("Enter the amount and quantity")
        amount = float(input("Enter amount: "))
        quantity = float(input("Enter quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more items(yes/no): ")
        if repeat.lower()== "no" :
            break

    print("_"*40)

    print("Name:",Name)
    print("Amount to be paid:", total)

    print("_"*40)

    print("*********Happy Shopping**********")

    repeat1 =input("Do you want to go next customer(yes/no): ")
    if repeat1.lower() == "no":
        break
print("Thank you")