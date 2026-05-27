def la_so_nguyen_to(n):

    if n < 2:
        return False

    for i in range(2, n):

        if n % i == 0:
            return False

    return True


def tim_snt_dau_tien(a):

    for i in range(len(a)):

        if la_so_nguyen_to(a[i]):

            print("So nguyen to dau tien la:", a[i])
            print("Vi tri:", i)
            return

    print("Khong co so nguyen to")


a = []

n = int(input("Nhap so phan tu: "))

for i in range(n):

    x = int(input("Nhap phan tu: "))
    a.append(x)

tim_snt_dau_tien(a)