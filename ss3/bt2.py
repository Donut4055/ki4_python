def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3 or n == 7 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    i = -1
    while i * i <= n:
        i += 6
        if n % (i) == 0 or n % (i + 2) == 0:
            return False
    return True


n = int(input("nhap vao 1 so: "))
if is_prime(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai so nguyen to")
