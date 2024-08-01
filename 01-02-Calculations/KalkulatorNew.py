import os
os.system('cls')
#os.system('color a')

username = ["Kak Ali", "Kak Galih", "Kak Asma", "Kak Aishah", "Jecy", "Arsya", "Dahayu", "Ardan", "Ilmi", "Nabil", "Fattan", "Faiz", "Fachri"]
password = "Praxis"

while True : # to username
        user = input("Masukkan Usename :")

        if user.lower() in (name.lower() for name in username) :
            print("Anda adalah salah satu anggota\nkeluarga kelas 10 SMA Praxis \n")
            print("Selamat Datang Di Kalkulator Kelas 10")
            break

        else :
            print("Anda bukan Keluarga kelas 10 SMA Praxis\nDILARANG MENGGUNAKAN KALKULATOR INI")
            continue

while True : # to Password
        print("SILAHKAN MASUKKAN PASSWORD")
        sandi = input("Password :")

        if sandi == password :
            print("Passsword Benar, lanjutkan...")
            break
        
        else :
            print("Password salah, coba lagi !!")
            continue

while True: # to operation sistem
    
    while True : # to input first number
        number1 = str(input("Masukkan Angka Pertama :"))
        
        if number1.isnumeric():
            print(f'Angka Pertama yang anda masukkan adalah : {number1}')
            break

        else:
            print("Angka Pertama yang anda masukkan tidak valid, coba lagi.")
            continue

    while True: # to select operation
        print("Silahkan Pilih Operasi")
        print("'+' = PENJUMLAHAN")
        print("'-' = PENGURANGAN")
        print("'*' = PERKALIAN")
        print("'/' = PEMBAGIAN")
        print("'^' = PERPANGKATAN")
        operasi = str(input("Masukkan Operasi ('+', '-', '*', '/', '^'):"))
        
        op = ["+", "-", "*", "/","^"]
        if operasi not in op : 
            print("operasi tidak valid")
            continue
        else : 
            break

    # for Operation options
    if operasi == "+" : 
        print("Operasi yang anda pilih adalah PENJUMLAHAN")

    elif operasi == "-" : 
        print("Operasi yang anda pilih adalah PENGURANGAN")

    elif operasi == "*" :
        print("Operasi yang anda pilih adalah PERKALIAN")

    elif operasi == "/" :
        print("Operasi yang anda pilih adalah PEMBAGIAN")
    
    elif operasi == "^" :
        print("Operasi yang anda pilih adalah PERPANGKATAN/EKSPONEN")

    while True : # to input second number
        number2 = str(input("Masukkan Angka Kedua :"))
        
        if number2.isnumeric():
            print(f'Angka kedua yang anda masukkan adalah : {number2}')
            break
        else:
            print("Angka yang anda masukkan tidak valid, coba lagi.")
            continue

    # to numeric operation
    if operasi == "+" : 
        result = int(number1) + int(number2)

    elif operasi == "-" : 
        result = int(number1) - int(number2)

    elif operasi == "*" :
        result = int(number1) * int(number2)

    elif operasi == "/" :
        result = int(number1) / int(number2)
    
    elif operasi == "^" :
        result = int(number1) ** int(number2)

        result = int
    print(f'Hasil dari {number1} {operasi} {number2} = {result}')

    while True : # to continue the system or not
        ulang = input("Apakah kamu mau berhitung lagi?? (ya/tidak) : ")

        if ulang.lower() == "tidak" :
            quit()
        
        elif ulang.lower() == 'ya':
            break

        else:
            print("Data tidak valid")
            continue
        
        

            




