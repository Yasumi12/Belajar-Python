# Operasi Komparasi

# Setiap hasil dari opeasi komparasi adalah boolean

# >,<,>=,>=,==,!=,is,is not

a = 5
b = 3

# Lebih Besar dari >
print("===== Lebih Besar dari (>) =====" )
hasil = a > 2
print(a,'>',2, '=', hasil)
hasil = b > 4
print(b,'>',4, '=', hasil)

# Kurang dari <
print("===== Kurang dari (<) =====" )
hasil = a < 2
print(a,'<',2, '=', hasil)
hasil = b < 4
print(b,'<',4, '=', hasil)

# lebih dari sama dengan >=
print("===== Lebih dari sama dengan (>=) =====" )
hasil = a >= 2
print(a,'>=',2, '=', hasil)
hasil = b >= 4
print(b,'>=',4, '=', hasil)
hasil = b >= 3
print(b,'>=',3, '=', hasil)

# Kurang dari sama dengan <=
print("===== Kurang dari sama dengan (<=) =====" )
hasil = a <= 2
print(a,'<=',2, '=', hasil)
hasil = b <= 4
print(b,'<=',4, '=', hasil)
hasil = b <= 3
print(b,'<=',3, '=', hasil)

# sama dengan ==
print("===== sama dengan (<=) =====" )
hasil = a == 5
print(a,'==',5, '=', hasil)
hasil = b == 5
print(b,'==',5, '=', hasil)

# Tidak sama dengan !=
print("===== sama dengan (!=) =====" )
hasil = a != 5
print(a,'!=',5, '=', hasil)
hasil = b != 5
print(b,'!=',5, '=', hasil)

# Operasi komparasi is dan is not hanya dapat digunakan untuk membandingkan object
x = 5
y = 6
print("x = ", x, hex(id(x)))
print("y = ", y, hex(id(y)))

hasil = x is y
print(x,'is',y, '=', hasil)

hasil = x is not y
print(x,'is not',y, '=', hasil)
