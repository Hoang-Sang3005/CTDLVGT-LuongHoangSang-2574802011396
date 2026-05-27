def gan_x_nhat(a, x):

    gan_nhat = a[0]
    vi_tri = 0

    for i in range(len(a)):

        if abs(a[i] - x) < abs(gan_nhat - x):

            gan_nhat = a[i]
            vi_tri = i

    print("Phan tu gan x nhat la:", gan_nhat)
    print("Vi tri:", vi_tri)


a = []

n = int(input("Nhap so phan tu: "))

for i in range(n):

    so = int(input("Nhap phan tu: "))
    a.append(so)

x = int(input("Nhap x: "))

gan_x_nhat(a, x)