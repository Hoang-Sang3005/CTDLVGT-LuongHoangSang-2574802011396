def tim_linh_canh(a, x):

    a.append(x)

    i = 0

    while a[i] != x:
        i += 1

    if i == len(a) - 1:
        return -1

    return i


a = []

n = int(input("Nhap so phan tu: "))

for i in range(n):

    so = int(input("Nhap phan tu: "))
    a.append(so)

x = int(input("Nhap x can tim: "))

print(tim_linh_canh(a, x))