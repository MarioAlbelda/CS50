def main():
    word = str(input("Input: "))
    print(f"Output: {shorten(word)}")

def shorten(word):
    shorted = ""
    for c in word:
        if(c not in "aeiouAEIOU"):
            shorted += c
    return shorted

if __name__ == "__main__":
    main()
