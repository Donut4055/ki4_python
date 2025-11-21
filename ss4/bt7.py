products = {"A": 120, "B": 80, "C": 300, "D": 50}

products = {
    k: v for k, v in products.items() if v < 100
}

print(products)
products["E"] = 100

print(products)
