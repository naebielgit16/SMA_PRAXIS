while True:
    # Meminta input angka pertama dengan validasi
    while True:
        try:
            number1 = float(input("Masukkan Angka Pertama: "))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # Meminta input operasi dengan validasi
    while True:
        operasi = input("Masukkan Operasi (+, -, *, /): ")
        if operasi in ["+", "-", "*", "/"]:
            break
        else:
            print("Operasi tidak benar. Harap masukkan salah satu dari (+, -, *, /).")

    # Meminta input angka kedua dengan validasi
    while True:
        try:
            number2 = float(input("Masukkan Angka Kedua: "))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # Melakukan operasi aritmatika berdasarkan input
    if operasi == "+":
        hasil = number1 + number2
    elif operasi == "-":
        hasil = number1 - number2
    elif operasi == "*":
        hasil = number1 * number2
    elif operasi == "/":
        try:
            hasil = number1 / number2
        except ZeroDivisionError:
            print("Pembagian dengan nol tidak diperbolehkan.")
            continue

    print(f"Hasil: {hasil}")

    # Menanyakan apakah user ingin melakukan perhitungan lagi
    ulang = input("Apakah kamu mau berhitung lagi? (ya/tidak): ").lower()
    if ulang != 'ya':
        break
