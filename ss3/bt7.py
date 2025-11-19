def reverse_number(n):
    temp = 0
    while n != 0:
        temp = temp * 10 + n % 10
        n = n // 10
    return temp


n = int(input("Nhap so: "))
print("So dao nguoc cua", n, "la", reverse_number(n))
