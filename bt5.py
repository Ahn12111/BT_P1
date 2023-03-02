# ham tinh tong cac so nguyen co hai chu so
def tong():
    tong = 0
    for i in range(10, 100):
        tong += i
    return tong


print("Tong cac chu so nguyen co hai chu so: {}".format(tong()))