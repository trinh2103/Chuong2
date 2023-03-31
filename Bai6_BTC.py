HoTen=input("Ho ten: ")
SoNgayCong=float(input("So ngay cong: "))
DonGiaNgayCong=float(input("Don gia ngay cong: "))
HeSoPhuCap=float(input("He so phu cap: "))
TamUng=int(input("Tam ung: "))
Luong=DonGiaNgayCong*SoNgayCong*HeSoPhuCap
ThucLinh=Luong-TamUng
print("Nhan vien "+HoTen+", Co tien Luong="+str(Luong)+", Tam ung="+str(TamUng)+" va Thuc linh="+str(ThucLinh))