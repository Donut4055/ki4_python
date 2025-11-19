def sum_of_digits(n):
    s = 0
    while n != 0:
        s = s + n % 10
        n = n // 10
    return s


n = int(input("Nhap so: "))
print("Tong cac chu so cua", n, "la", sum_of_digits(n))
