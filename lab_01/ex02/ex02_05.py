so_gio_lam = int(input("Nhập số giờ làm hàng tuần: "))
luong_gio = float(input("Nhập lương mỗi giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(so_gio_lam - gio_tieu_chuan, 0)
luong = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print("Lương hàng tuần của bạn là: ", luong)



