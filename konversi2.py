def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    suhu_input = input("Masukkan data suhu: ")
    
    if suhu_input[-1].upper() == 'C':
        suhu = float(suhu_input[:-1])
        hasil = celsius_ke_fahrenheit(suhu)
        print(f"{suhu} Celsius dikonversi ke Fahrenheit adalah {hasil} F")
    elif suhu_input[-1].upper() == 'F':
        suhu = float(suhu_input[:-1])
        hasil = fahrenheit_ke_celsius(suhu)
        print(f"{suhu} Fahrenheit dikonversi ke Celsius adalah {hasil} C")
    else:
        print("Suhu tidak valid. ")
        return  
    
    
    suhu_input = input("\nMasukkan data suhu lainnya: ")
    if suhu_input[-1].upper() == 'C':
        suhu = float(suhu_input[:-1])
        hasil = celsius_ke_fahrenheit(suhu)
        print(f"{suhu} Celsius dikonversi ke Fahrenheit adalah {hasil} F")
    elif suhu_input[-1].upper() == 'F':
        suhu = float(suhu_input[:-1])
        hasil = fahrenheit_ke_celsius(suhu)
        print(f"{suhu} Fahrenheit dikonversi ke Celsius adalah {hasil} C")
    else:
        print("Suhu tidak valid.")

if __name__ == "__main__":
    main()

