# Viết chương trình tính tổng của các chữ số của một số nguyên n trong python. Số nguyên n được nhập từ bàn phím
# Với n = 1234, tổng các chữ số:: 1 + 2 + 3 + 4 = 10

"""
* Tính tổng các chữ số của một số nguyên dương n
*
* @param vantruong: số nguyên dương
* @return
"""
def tinhtong(vantruong):
    total = 0;
    while (vantruong > 0):
        total = total + vantruong % 10;
        vantruong = int(vantruong / 10);
    return total;

truong = input("Tên:")
vantruong = int(input("Nhập số nguyên dương n = "));
print("tổng các chữ số ", vantruong, " là ", tinhtong(vantruong));