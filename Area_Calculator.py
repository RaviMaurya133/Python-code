print("---- Area Calculator ----")

while True:
    print("""Press 1, If you want to calculate the area of the square,
Press 2, If you want to calculate the area of the rectangle,
Press 3, If you want to calculate the area of the circle,
Press 4, If you want to calculate the area of the triangle""")
    print("-" * 30)

    n = int(input("Enter your number here (1 to 4): "))

    if n == 1:
        while True:
            side = int(input("Enter length of side: "))
            area = side ** 2
            print("The area of the square is:", area)

            while True:
                repeat = input("Do you want to try again with square: ").lower()
                if repeat == "yes":
                    break
                elif repeat == "no":
                    break_outer = True
                    break
                else:
                    print("This is invalid input, Please click valid input.")
            if repeat == "no":
                break
            print("-" * 30)

    elif n == 2:
        while True:
            length = int(input("Enter length of rectangle: "))
            width = int(input("Enter width of rectangle: "))
            area = length * width
            print("The area of the rectangle is:", area)

            while True:
                repeat = input("Do you want to try again with rectangle: ").lower()
                if repeat == "yes":
                    break
                elif repeat == "no":
                    break_outer = True
                    break
                else:
                    print("This is invalid input, Please click valid input.")
            if repeat == "no":
                break
            print("-" * 30)

    elif n == 3:
        while True:
            radius = int(input("Enter the radius of the circle: "))
            area = (22/7) * radius ** 2
            print("The area of the circle is:", area)

            while True:
                repeat = input("Do you want to try again with circle: ").lower()
                if repeat == "yes":
                    break
                elif repeat == "no":
                    break_outer = True
                    break
                else:
                    print("This is invalid input, Please click valid input.")
            if repeat == "no":
                break
            print("-" * 30)

    elif n == 4:
        while True:
            height = int(input("Enter the height of triangle: "))
            base = int(input("Enter the base of the triangle: "))
            area = 0.5 * base * height
            print("The area of the triangle is:", area)

            while True:
                repeat = input("Do you want to try again with triangle: ").lower()
                if repeat == "yes":
                    break
                elif repeat == "no":
                    break_outer = True
                    break
                else:
                    print("This is invalid input, Please click valid input.")
            if repeat == "no":
                break
            print("-" * 30)

    else:
        print("This is invalid input, Please click valid input.")
    print("-"*30)

    while True:
        repeat1 = input("Do you want to repeat menu again: ").lower()
        if repeat1 == "yes":
            break
        elif repeat1 == "no":
            exit()
        else:
            print("This is invalid input, Please click valid input.")
