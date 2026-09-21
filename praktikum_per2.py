#1. Write a PYTHON program to evaluate the student performance
# masukkan dan deklarasi dulu variable nya

nilai = int(input("Masukkan nilai: "))
#setelah di deklarasi maka kita tambahakan variable tersebut ke kondisi untuk menyimpan data
if nilai >= 90:
    print("excelent")
elif nilai >= 80:
    print("very good")
elif nilai >= 70:
    print("good")
elif nilai >= 60:
    print("average")
else:
    print("LEBIH GIAT LAGI")

    
#2. Write a PYTHON program to find largest of three numbers!
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

if angka1 >= angka2 and angka1 >= angka3:
    print("Angka terbesar adalah:", angka1)
elif angka2 >= angka1 and angka2 >= angka3:
    print("Angka terbesar adalah:", angka2)
else:
    print("Angka terbesar adalah:", angka3)

