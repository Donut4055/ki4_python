n = int(input("nhap vao 1 so nguyen: "))
mark = n
temp = 0
while n != 0:
    print(n)
    temp = temp * 10 + n % 10
    n = n // 10
if mark == temp:
    print("n la so doi xung")
else:
    print("n khong phai la so doi xung")
