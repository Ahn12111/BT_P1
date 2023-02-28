import math

r = float(input("Nhap ban kinh hinh tru: "))
h = float(input("Nhap chieu cao hinh tru: "))

print("The tich hinh tru: ", math.pi * r * r *h)
print("Dien tich xung quanh hinh tru: ", 2 * math.pi * r* h)