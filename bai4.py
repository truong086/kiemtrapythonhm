# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách
# và một tuple chứa mọi số

vantruong=input("Enter student code")
van=vantruong.split(",")
truong=tuple(van)
print (van)
print (truong)