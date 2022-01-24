# operasi aritmatika

# Penjumlahan +
a = 10
b = 7
hasil = a + b
print(a,'+',b, '=', hasil)

# Pengurangan -
hasil = a - b
print(a,'-',b, '=', hasil)

# Perkalian *
hasil = a * b
print(a,'x',b, '=', hasil)

# Pembagian /
hasil = a / b
print(a,':',b, '=', hasil)

# Perpangkatan (eskponen) **
hasil = a ** b
print(a,'**',b, '=', hasil)

# modulus %
hasil = a % b
print(a,'%',b, '=', hasil)

# floor division //
hasil = a // b
print(a,'//',b, '=', hasil)

# Prioritas operasi, Operational Precedence
'''
    1. ()
    2. eksponen **
    3. Perkalian dan teman-temannya * / % //
    4. Penjumlahan + -
'''

x = 5
y = 3
z = 2

hasil = x * y + z
print(x,'*',y,'+',z,'=', hasil)

hasil = x * (y + z)
print(x,'* (',y,'+',z,') =', hasil)
