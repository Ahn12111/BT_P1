import math

x = float(input("Nhap x: "))
if (math.exp(2 * x) + math.cos(math.pi * x / 4) == 0):
    printf("Bieu thuc khong xac dinh")
else:
    y1 = 4 * (pow(x, 2) + 10 * x * pow(x, 1 / 2) + 3 * x + 1)
    y2 = (math.sin(math. pi * x * x) + pow(x * x + 1, 1 / 2)) / \
        (math.exp(2 * x) + math.cos(math.pi * x / 4))
    print("gia tri bieu thuc y1 = %.3f" % (y1))
    print("gia tri bieu thuc y2 = %.15f" % (y2))