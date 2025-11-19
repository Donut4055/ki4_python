PI = 3.14159


def circle_area(radius):
    return PI * radius * radius


r = float(input("Nhap ban kinh hinh tron: "))
print("Dien tich hinh tron la: ", circle_area(r))
