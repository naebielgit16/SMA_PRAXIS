# Firt exercise
prime = [2,3,5,7]

prime_min = min(prime) 
prime_max = max(prime)

print("Soal ke-1 :")
print(f"Nilai = {prime}")
print(f"Nilai minimumnya adalah : {prime_min}")
print(f"Nilai minimumnya adalah : {prime_max}\n") 
 

# Second exercise (budimukidi)
# data = "budimukidi"
# char = {}

# for i in data :
#     if char in data:
#         char[data] += 1
#     else :
#         char[data] = 1

#test AI:

# Menentukan string yang akan dihitung kemunculan karakternya

data = "ubur-ubur"
print("Soal ke-2 :")
# Menginisialisasi dictionary kosong untuk menyimpan jumlah kemunculan karakter
char = {}

print(f"Data = {data}")
# Menghitung kemunculan setiap karakter dalam string
for i in data:
    if i in char:
        char[i] += 1
    else:
        char[i] = 1

# Mencetak hasil
for karakter, jumlah in char.items():
    print(f"Karakter '{karakter}' muncul sebanyak {jumlah} kali")


# Third exercise (Tambahkan sebuah key & value pada sebuah dictionary)
print("\nSoal ke-3 :")
dict = {
    0 : "Nabil",
    1 : "Faiz"
}

dict[2] = "Dzaki"
print(dict)

