def factorial(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s


n = int(input("nhap vao 1 so: "))
print("giai thua cua", n, "la ", factorial(n))
