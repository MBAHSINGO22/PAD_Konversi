def byte_ke_kb(byte):
    return byte / 1024

def byte_ke_mb(byte):
    return byte / (1024 ** 2)

def byte_ke_gb(byte):
    return byte / (1024 ** 3)

def byte_ke_tb(byte):
    return byte / (1024 ** 4)

def kb_ke_byte(kb):
    return kb * 1024

def mb_ke_byte(mb):
    return mb * (1024 ** 2)

def gb_ke_byte(gb):
    return gb * (1024 ** 3)

def tb_ke_byte(tb):
    return tb * (1024 ** 4)

def main():
    data = input("Masukkan data: ")
    value, unit = data.split()
    value = float(value)
    
    print("Mau dikonversi ke:")
    print("1. Byte")
    print("2. Kilobyte")
    print("3. Megabyte")
    print("4. Gigabyte")
    print("5. Terabyte")
    
    choice = int(input("Pilihan Anda: "))
    
    if choice == 1:
        if unit.upper() == "KB":
            print(f"{value} KB dikonversi ke Byte adalah {kb_ke_byte(value)} B")
        elif unit.upper() == "MB":
            print(f"{value} MB dikonversi ke Byte adalah {mb_ke_byte(value)} B")
        elif unit.upper() == "GB":
            print(f"{value} GB dikonversi ke Byte adalah {gb_ke_byte(value)} B")
        elif unit.upper() == "TB":
            print(f"{value} TB dikonversi ke Byte adalah {tb_ke_byte(value)} B")
        else:
            print("Tidak valid")
    elif choice == 2:
        if unit.upper() == "BYTE":
            print(f"{value} B dikonversi ke Kilobyte adalah {byte_ke_kb(value)} KB")
        elif unit.upper() == "MB":
            print(f"{value} MB dikonversi ke Kilobyte adalah {mb_ke_byte(value)} KB")
        elif unit.upper() == "GB":
            print(f"{value} GB dikonversi ke Kilobyte adalah {gb_ke_byte(value)} KB")
        elif unit.upper() == "TB":
            print(f"{value} TB dikonversi ke Kilobyte adalah {tb_ke_byte(value)} KB")
        else:
            print("Tidak valid")
    elif choice == 3:
        if unit.upper() == "BYTE":
            print(f"{value} B dikonversi ke Megabyte adalah {byte_ke_mb(value)} MB")
        elif unit.upper() == "KB":
            print(f"{value} KB dikonversi ke Megabyte adalah {kb_ke_byte(value)} MB")
        elif unit.upper() == "GB":
            print(f"{value} GB dikonversi ke Megabyte adalah {gb_ke_byte(value)} MB")
        elif unit.upper() == "TB":
            print(f"{value} TB dikonversi ke Megabyte adalah {tb_ke_byte(value)} MB")
        else:
            print("Tidak valid")
    elif choice == 4:
        if unit.upper() == "BYTE":
            print(f"{value} B dikonversi ke Gigabyte adalah {byte_ke_gb(value)} GB")
        elif unit.upper() == "KB":
            print(f"{value} KB dikonversi ke Gigabyte adalah {kb_ke_byte(value)} GB")
        elif unit.upper() == "MB":
            print(f"{value} MB dikonversi ke Gigabyte adalah {mb_ke_byte(value)} GB")
        elif unit.upper() == "TB":
            print(f"{value} TB dikonversi ke Gigabyte adalah {tb_ke_byte(value)} GB")
        else:
            print("Tidak valid")
    elif choice == 5:
        if unit.upper() == "BYTE":
            print(f"{value} B dikonversi ke Terabyte adalah {byte_ke_tb(value)} TB")
        elif unit.upper() == "KB":
            print(f"{value} KB dikonversi ke Terabyte adalah {kb_ke_byte(value)} TB")
        elif unit.upper() == "MB":
            print(f"{value} MB dikonversi ke Terabyte adalah {mb_ke_byte(value)} TB")
        elif unit.upper() == "GB":
            print(f"{value} GB dikonversi ke Terabyte adalah {gb_ke_byte(value)} TB")
        else:
            print("Tidak valid")
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
