import os
os.system('cls')
os.system('color a')

username = ["Kak Ali", "Kak Galih", "Kak Asma", "Kak Aishah", "Jecy", "Arsya", "Dahayu", "Ardan", "Ilmi", "Nabil", "Fattan", "Faiz", "Fachri"]
password = "level 10"
while True:
    while True : 
        user = input("Masukkan Usename :")

        if user.lower() in (name.lower() for name in username) :
            print("Anda adalah keluarga kelas 10 SMA Praxis")
            break

        else :
            print("Anda bukan Keluarga kelas 10 SMA Praxis")
            continue

    while True :
        sandi = input("Masukkan Password :")

        if sandi == password :
            print("Passsword Benar")
            break
        
        else :
            print("Password salah, coba lagi !")
            continue
    
    while True :
        number1 = str(input("Masukkan Angka Pertama :"))
        
        if number1.isnumeric():
            print(f'Angka yang anda masukkan adalah : {number1}')
            break

        else:
            print("Angka Pertama yang anda masukkan tidak valid, coba lagi.")
            continue

    while True: #operasi
        operasi = str(input("Masukkan Operasi ('+', '-', '*', '/'):"))
        op = ["+", "-", "*", "/"]
        if operasi not in op : 
            print("operasi tidak valid")
            continue
        else: 
            break

    while True :
        number2 = str(input("Masukkan Angka Kedua :"))
        
        if number2.isnumeric():
            print(f'Angka kedua yang anda masukkan adalah : {number2}')
            break
        else:
            print("Angka yang anda masukkan tidak valid, coba lagi.")
            continue

            
    if operasi == "+" : 
        result = int(number1) + int(number2)

    elif operasi == "-" : 
        result = int(number1) - int(number2)

    elif operasi == "*" :
        result = int(number1) * int(number2)

    elif operasi == "/" :
        result = int(number1) / int(number2)

    print(f'Hasil dari {number1} {operasi} {number2} = {result}')

    while True :
        ulang = input("Apakah kamu mau berhitung lagi?? (ya/tidak) : ")

        if ulang.lower() == "tidak" :
            quit()
        
        elif ulang.lower() == 'ya':
            break

        else:
            continue
        
        

            




