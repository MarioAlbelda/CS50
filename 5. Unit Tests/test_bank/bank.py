def main():

    greeting = input("Greeting: ")
    payment = value(greeting)
    print(f"${payment}")

def value(greeting):

    greet = greeting.strip().lower()

    if greet.startswith("hello"):
        return(int(0))
    elif greet.startswith("h"):
        return(int(20))
    else:
        return(int(100))

if __name__ == "__main__":
    main()
