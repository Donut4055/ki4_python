a = input("nhap vao 1 so nguyen: ")
n = int(a)

if (n % 3 == 0) and (n % 5 == 0):
    print("chia het cho 3 va 5")
else:
    if n % 5 == 0:
        print("chia het cho 5")
    else:
        if n % 3 == 0:
            print("khong chia het cho 3")
      
