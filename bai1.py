fullname = input("enter any name =")
n = len(fullname)

vantruong = dict()
vantruong["name"] = fullname
for i in range(1, n + 1):
    vantruong[i] = i * i
print(vantruong)