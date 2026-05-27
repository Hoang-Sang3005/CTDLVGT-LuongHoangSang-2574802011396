def ton_tai(a,x):
    for i in range(len(a)):
        if a[i]==x:
            return True
    return False
n = int(input("nhap list:"))

a = []
for i in range(n):
    so = int(input(f"nhap phan tu thu {i + 1}:"))
    a.append(so)

    



x = int(input("nhap phan tu can tim"))

ket_qua = ton_tai(a,x)

