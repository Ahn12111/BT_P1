import datetime
dt = datetime.datetime.now()

n = int(input("Nhap nam sinh cua ban: "))
print("Ban sinh nam: ", n)
print("Vay ban ",dt.year - n, " tuoi")
#dt.year là năm hiện tại lấy từ thư viện datetime