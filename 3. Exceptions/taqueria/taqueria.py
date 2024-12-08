prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

Total = float(0)


while True:
    try:
        item = str(input("Item: ")).title()

    except EOFError:
        print("")
        break
    else:
        if item in prices:
            x = float(prices[item])
            Total += x
            print(f"${Total:.2f}")
