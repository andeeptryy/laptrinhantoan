print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines=[]
while True:
    line=input()
    if line=="done":
        break
    lines.append(line)
    
    print("\nCac dong ban vua nhap sau khi chuyen thanh chu in hoa la:")
    for line in lines:  
        print(line.upper())