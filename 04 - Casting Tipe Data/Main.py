# Casting
# Merubah tipe data satu ke tipe data lain
# Tipe data : str, float, int, bool

# Integer
print("====INTEGER====")
data_int = 2
print("data = ", data_int, " Tipe = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # Akan bernilai false jika nilai int = 0
print("data = ", data_float, " Tipe = ", type(data_float))
print("data = ", data_str, " Tipe = ", type(data_str))
print("data = ", data_bool, " Tipe = ", type(data_bool))

# Float
print("====FLOAT====")
data_float = 3.5
print("data = ", data_float, " Tipe = ", type(data_float))

data_int = int(data_float) # Akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # Akan bernilai false jika nilai float = 0
print("data = ", data_int, " Tipe = ", type(data_int))
print("data = ", data_str, " Tipe = ", type(data_str))
print("data = ", data_bool, " Tipe = ", type(data_bool))

# Boolean
print("====BOOLEAN====")
data_bool = True
print("data = ", data_bool, " Tipe = ", type(data_bool))

data_int = int(data_bool) # akan bernilai 0 jika bool false
data_str = str(data_bool) # Akan bernilai sama dengan bool
data_float = float(data_bool) # akan bernilai 0 jika bool false
print("data = ", data_int, " Tipe = ", type(data_int))
print("data = ", data_str, " Tipe = ", type(data_str))
print("data = ", data_float, " Tipe = ", type(data_float))

# String
print("====STRING====")
data_str= "10"
print("data = ", data_str, " Tipe = ", type(data_str))

data_int = int(data_str) # String harus angka
data_bool = bool(data_str) # False jika str kosong
data_float = float(data_str) # string harus angka
print("data = ", data_int, " Tipe = ", type(data_int))
print("data = ", data_bool, " Tipe = ", type(data_bool))
print("data = ", data_float, " Tipe = ", type(data_float))
