from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        if self.soLuongSinhVien() == 0:
            return 1
        else:
            maxID = max(sv.id for sv in self.listSinhVien)
            return maxID + 1

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.diemTB)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv.id == ID:
                return sv
        return None

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.lower() in sv.name.lower()]

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv.diemTB >= 8:
            sv.hocluc = "Gioi"
        elif sv.diemTB >= 6.5:
            sv.hocluc = "Kha"
        elif sv.diemTB >= 5:
            sv.hocluc = "Trung binh"
        else:
            sv.hocluc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<5} {:<18} {:<8} {:<12} {:<10} {:<10}".format(
            "ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        for sv in listSV:
            print("{:<5} {:<18} {:<8} {:<12} {:<10} {:<10}".format(
                sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
