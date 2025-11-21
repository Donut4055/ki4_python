products = {"A": 120, "B": 80, "C": 300, "D": 50}

if "A" in products:
    print(products["A"])
else:
    print("Không có sản phẩm A")

sorted_product = dict(sorted(products.items(), key=lambda item: item[1]))

print(sorted_product)

products = {
    k: v for k, v in products.items() if v < 200
}
print(products)
