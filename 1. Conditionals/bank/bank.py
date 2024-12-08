def main():
    greeting = input("Greeting: ").strip().lower()

    if hello(greeting):
        print("$0")
    elif h(greeting):
        print("$20")
    else:
        print("$100")

def hello(greeting):
    return greeting.startswith("hello")

def h(greeting):
    return greeting.startswith("h")

main()
