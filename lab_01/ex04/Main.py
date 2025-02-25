from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()

while (1 == 1) :
    print(" =================== QUẢN LÝ SINH VIÊN =====================")
    print(" ***********************************************************")
    print(" *      1. Thêm                                            *")
    print(" *      2. Sửa                                             *")
    print(" *      3. Xóa                                             *")
    print(" *      4. Tìm kiếm theo Tên                               *")
    print(" *      5. SX theo DTB                                     *")
    print(" *      6. SX theo Ten CN                                  *")
    print(" *      7. Hiển thị DSSV                                   *")
    print(" *      8. Thoát                                           *")
    print(" ***********************************************************")

    key = int(input("Mời bạn chọn chức năng: "))
    if key == 1:
        print("Thêm sinh viên")
        qlsv.themSinhVien()
        print("Thêm sinh viên thành công: ")
    elif key == 2:
        if(qlsv.soLuongSinhVien() > 0):
            print('\n2. Cập nhật thông tin sinh viên')
            print("Nhập ID: ")
            ID = int(input())
            qlsv.capNhatSinhVien(ID)
        else:
            print("Danh sách sinh viên rỗng. Mời bạn thêm sinh viên!")
    elif key == 3:
        if(qlsv.soLuongSinhVien() > 0):
            print('\n3. Xóa sinh viên')
            print("Nhập ID: ")
            ID = int(input())
            if(qlsv.xoaSinhVien(ID)):
                print("Xóa sinh viên thành công!")
            else:
                print("Không tồn tại")
        else:
            print("Danh sách sinh viên rỗng. Mời bạn thêm sinh viên!")     
    elif key == 4:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên")   
            print("\nNhập tên sinh viên cần tìm: ")
            name = input()
            searchResult = qlsv.timKiemTheoTen(name)
            qlsv.ShowSV(searchResult)
        else:
            print("Danh sách sinh viên rỗng. Mời bạn thêm sinh viên!") 
    elif key == 5:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình")
            qlsv.sapXepTheoDTB()
            qlsv.ShowSV(qlsv.listSV())
        else:
            print("Danh sách sinh viên rỗng. Mời bạn thêm sinh viên!")
    elif key == 6:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên chuyên ngành")
            qlsv.sapXepTheoTenCN()
            qlsv.ShowSV(qlsv.listSV())
        else:
            print("Danh sách sinh viên rỗng. Mời bạn thêm sinh viên!")
    elif key == 7:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.ShowSV(qlsv.listSV())
        else:
            print("Danh sách sinh viên rỗng. Mời bạn thêm sinh viên!")
           
    elif key == 8:
        break
    else:
        print("Chức năng không tồn tại. Mời bạn chọn lại!")