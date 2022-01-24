# Tipe data: integer (angka)
data = 1
print("data : ", data, ", Bertipe: ", type(data))


# Tipe data : float (desimal)
data_float = 1.25
print("data: ", data_float, ", Bertipe: ", type(data_float))


# Tipe data : string (Kumpulan karakter)
data_string = "Akbar"
print("data: ", data_string, ", Bertipe: ", type(data_string))


# Tipe data : boolean (biner)
data_bool = True
print("data: ", data_bool, ", Bertipe: ", type(data_bool))


# Tipe data khusus
# Tipe data kompleks
data_kompleks = complex(7,2)
print("data: ", data_kompleks, ", Bertipe: ", type(data_kompleks))

# Mengambil tipe data C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data: ", data_c_double, ", Bertipe: ", type(data_c_double))
