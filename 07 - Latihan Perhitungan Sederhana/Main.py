# Latihan konversi satuan temperatur

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# Program konversi celcius ke satuan lain
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu celcius adalah ", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu reamur adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu fahrenheit adalah ", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu kelvin adalah ", kelvin, "Kelvin")

# Konversi Reamur ke satuan lain
reamur = float(input("Masukkan suhu dalam reamur: "))
print("Suhu reamur adalah ", reamur, "Reamur")

# Celcius
celcius = (5/4) * reamur
print("Suhu celcius adalah ", celcius, "Celcius")

# fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu fahrenheit adalah ", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = ((5/4) * reamur) + 273
print("Suhu kelvin adalah ", kelvin, "Kelvin")


# Konversi Fahrenheit ke satuan lain
fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
print("Suhu fahrenheit adalah ", fahrenheit, "Fahrenheit")

# Celcius
celcius = 5/9 * (fahrenheit - 32)
print("Suhu celcius adalah ", celcius, "Celcius")

# Reamur
reamur = 4/9 * (fahrenheit - 32)
print("Suhu reamur adalah ", reamur, "Reamur")

# Kelvin
kelvin = celcius + 273
print("Suhu kelvin adalah ", kelvin, "Kelvin")


# Kelvin ke satuan lain
kelvin = float(input("Masukkan suhu dalam kelvin: "))
print("Suhu kelvin adalah ", kelvin, "Kelvin")

# Celcius
celcius = kelvin - 273
print("Suhu celcius adalah ", celcius, "Celcius")

# Reamur
reamur = 4/5 * (celcius)
print("Suhu reamur adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = (9/5 * (celcius)) + 32
print("Suhu fahrenheit adalah ", fahrenheit, "Fahrenheit")


