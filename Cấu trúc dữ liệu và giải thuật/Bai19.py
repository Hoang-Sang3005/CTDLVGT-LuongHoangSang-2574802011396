ds = [
    {"ma": "SV01", "ten": "An", "dtb": 8},
    {"ma": "SV02", "ten": "Binh", "dtb": 7},
    {"ma": "SV03", "ten": "Chau", "dtb": 9}
]

ma_can_tim = input("Nhap ma sinh vien: ")

tim_thay = False

for sv in ds:

    if sv["ma"] == ma_can_tim:

        print("Ma:", sv["ma"])
        print("Ten:", sv["ten"])
        print("DTB:", sv["dtb"])

        tim_thay = True
        break


if tim_thay == False:
    print("Khong tim thay")