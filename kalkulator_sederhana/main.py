import kalkulator

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

print("Hasil Penjumlahan :", kalkulator.tambah(angka1, angka2))
print("Hasil Pengurangan :", kalkulator.kurang(angka1, angka2))
print("Hasil Perkalian   :", kalkulator.kali(angka1, angka2))
print("Hasil Pembagian   :", kalkulator.bagi(angka1, angka2))