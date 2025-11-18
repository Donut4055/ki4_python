a = int(input("nhap vao 1 so nguyen: "))
b = int(input("nhap vao 1 so nguyen: "))
c = int(input("nhap vao 1 so nguyen: "))

if a + b > c and a + c > b and b + c > a:
    print(" la 3 canh cua mot tam giac")
else:
    print(" khong phai la 3 canh cua mot tam giac")
