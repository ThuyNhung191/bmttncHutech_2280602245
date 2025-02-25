def TongCacSoChan(a) :
    sum = 0
    for i in a:
        if i%2==0:
            sum=sum+i
    return sum

input_list = input("Nhập vào danh sách các số cách nhau bởi dấu (,): ")
a = list(map(int , input_list.split(",")))

print(" Tổng các số chẵn có trong mảng: ", TongCacSoChan(a))