print("Amount Due: 50")
i = 50

while i > 0:
    coin = int(input("Insert coin: "))
    if coin in (25, 10, 5):
        i -= coin
        if i > 0:
            print(f"Amount Due: {i}")
    else:
        print(f"Amount Due: {i}")

print(f"Change Owed: {-i}")
