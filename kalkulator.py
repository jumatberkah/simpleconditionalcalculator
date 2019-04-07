import sys


def testing():
    print ("Selamat Datang di Program Kalkulator dengan prinsip Kondisional Sederhana")
    opsimasuk = input("Pilih Opsi: [Mulai/Tidak]")
    if opsimasuk == "Tidak":
        sys.exit()
    elif opsimasuk == "Mulai" or "mulai" :
        print ("Selamat Mencoba! Ikuti perintah yang diberikan!")
        nilai = input("Masukkan angka untuk dioperasikan:")
        operasi = input("Tulislah operasi yang diinginkan: [tambah/kali/bagi/kurang/pangkat/akar]")
        nilaikedua = input("Masukkan Nilai Kedua:")
        if operasi == "tambah":
            hasil = (float(nilai)) + (float(nilaikedua))
            print (hasil)
        elif operasi == "kurang":
            hasil = (float(nilai)) - (float(nilaikedua))
            print (hasil)
        elif operasi == "kali":
            hasil = (float(nilai)) * (float(nilaikedua))
            print (hasil)
        elif operasi == "bagi":
            hasil = (float(nilai)) / (float(nilaikedua))
            print (hasil)
        elif operasi == "pangkat":
            hasil = (float(nilai)) ** (float(nilaikedua))
            print (hasil)
        elif operasi == "akar":
            hasil = (float(nilai)) // (float(nilaikedua))
            print (hasil)


testing()
