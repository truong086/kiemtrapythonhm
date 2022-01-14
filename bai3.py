# Viết chương trình kiểm một số n là số thuận nghịch trong python. Số nguyên dương n được nhập từ bàn phím

"""
* Kiểm tra số thuận nghịch
"""

truong = input("Nhập số:  ")
def hamkiemtra(truong):
    truong1 = str(truong);     # ep kieu so n thanh chuoi
    truong2 = truong1[::-1];
    if (truong1 == truong2):
        print(truong," là một số thuận nghịch")
    else:
        print(truong," không là một số thuận nghịch")
hamkiemtra(truong)

vantruong = input("Fullname: ")