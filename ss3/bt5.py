def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


n = int(input("Nhap nam: "))
if is_leap_year(n):
    print(n, "la nam nhuận")
else:
    print(n, "khong phai nam nhuận")
