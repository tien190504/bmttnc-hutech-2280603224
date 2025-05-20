so_gio_lam = float(input("Nhap so gio lam moi tuan: "))
luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chua = 44
gio_vuot_chua = max(0, so_gio_lam - gio_tieu_chua)
thuc_linh = gio_tieu_chua * luong_gio + gio_vuot_chua * luong_gio * 1.5

print(f"So tien thuc linh cua nhan vien la: {thuc_linh}")
