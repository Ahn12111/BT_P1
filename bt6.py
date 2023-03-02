def xuly():
    global list1, list2
    # Truy cập đến từng phần tử trong mảng list1
    for i in range(len(list1)):
        j = 0
        # kiểm tra xem tờ tiền thứ i đã xuất hiện hay chưa
        while (j < i):
            if(list1[i] == list1[j]):
                break
            j += 1
        # dem so tien đó
        list2[j] += 1

    for i in range(len(list2)):
        if (list2[i] != 0):
            print(list1[i], " đồng có ", list2[i], " tờ tiền")

# HÀM MAIN():
print("Nhập các tờ tiền (hãy nhập '-1' khi muốn kết thúc): ")
list1 = []
list2 = []

while True:
    i = int(input())
    if (i == -1):
        break
    else:
        # lưu các tờ tiền vào mảng list1
        list1.append(i)
        # tạo một mảng phụ có các phần tử là 0 mục đích để đếm số tờ tiền giống nhau
        list2.append(0)
xuly()

