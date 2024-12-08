fruit = str(input("Item: ")).lower()

raw_fruits = {
    "apple": "130",
    "avocado": "50",
    "cantaloupe": "50",
    "honeydew melon": "50",
    "pineapple": "50",
    "strawberries": "50",
    "tangerine": "50",
    "banana": "110",
    "grapefruit": "60",
    "nectarine": "60",
    "peach": "60",
    "grapes": "90",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "orange": "80",
    "watermelon": "80",
    "pear": "100",
    "sweet cherries": "100",
    "plums": "70",
}

if fruit in raw_fruits:
    print("Calories: ", raw_fruits[fruit])
