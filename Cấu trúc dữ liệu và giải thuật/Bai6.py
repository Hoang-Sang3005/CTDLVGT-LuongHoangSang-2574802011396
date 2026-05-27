def linear_search(a , x):
    for i in range(len(a)):
        if a[i] == x:
            return i
        return -1
n = int(input("Nhap phan tu cua mang"))

a = []
for i in range(n):
    so = int(input(f"nhap phan tu thu {i + 1}:"))
    a.append(so)

x = int(input("Nhap gia tri can tim:"))

ket_qua = linear_search(a , x)
if ket_qua != -1:
    print(f"Phan tu duoc tim thay o vi tri thu {ket_qua} trong mang")
else:
    print("Khong tim thay")

