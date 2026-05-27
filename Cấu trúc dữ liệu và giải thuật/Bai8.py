def xuat_hien(a):
    count = 0

    x = int(input("Nhap x: "))

    for i in a:
        if i == x:
            count += 1

    return count


a = [1, 2, 3, 2, 4, 2]

print("So lan xuat hien:", xuat_hien(a))
