# Input data user

# data yang dimasukkan pasti bertipe string

data = input("Masukkan data: ")
print("data = ", data, ",",type(data))

# Jika ingin mengambil  data int, maka
angka = int(input("Masukkan angka: "))
angka1 = float(input("Masukkan angka: "))

print("data = ", angka, ",", type(angka))
print("data = ", angka1, ",", type(angka1))

# Data boolean

biner = bool(int(input("Masukkan boolean: ")))
print("data = ", biner, ",", type(biner))
