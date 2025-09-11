so_gio_lam=float (input("Nhap so gio lam moi tuan: "))
luong_gio=float (input("Nhap thu lao tren moi luong gio lam tieu chuan: "))
gio_tieu_chuan=44 
gio_vuot_chuan=max(0, so_gio_lam-gio_tieu_chuan)
thuc_linh=luong_gio*gio_tieu_chuan+luong_gio*1.5*gio_vuot_chuan
print(f"So tien thuc linh cua nhan vien la:", {thuc_linh})