
def DaoNguocChuoi(chuoi) :
    return chuoi[::-1]

input_string = input("Nhập vào chuỗi cần đảo ngược: ")
print("Chuỗi sau khi đảo ngược là: ", DaoNguocChuoi(input_string))