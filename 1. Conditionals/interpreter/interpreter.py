expression = input("Expression: ")

x, y, z = expression.split(" ")

match y:
    case "+":
        print(float(int(x) + int(z)))
    case "-":
        print(float(int(x) - int(z)))
    case "*":
        print(float(int(x) * int(z)))
    case "/":
        print(float(int(x) / int(z)))
