def perfect_number(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


n = int(input("Nhap so: "))
if perfect_number(n):
    print(n, "la so hoan hao")
else:
    print(n, "khong phai so hoan hao")
