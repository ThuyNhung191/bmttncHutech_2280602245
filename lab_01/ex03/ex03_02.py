def daonguocmang(x):
    return x[::-1]

nhap = input("Nhập vào danh sách các số , Cách nhau bởi dấu: ")
number = list(map(int, nhap.split(",")))

list_dao = daonguocmang(number)
print(" List sau khi đảo ngươc: ", list_dao)