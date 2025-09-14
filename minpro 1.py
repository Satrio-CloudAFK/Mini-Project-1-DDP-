# Program sederhana: Manajemen 6 bilik kamar mandi

# Data awal
bilik_tersedia = [1, 2, 3, 4, 5, 6]
bilik_terpakai = []

while True:
    print("====== KETERSEDIAAN BILIK KAMAR MANDI ======")
    print(f"Bilik tersedia : {bilik_tersedia}")
    print(f"Bilik terpakai : {bilik_terpakai}")
    print("="*43)
    print("1 = Masuk Bilik")
    print("2 = Keluar Bilik")
    print("3 = Reset")
    print("===========================================")

    pilihan = input("\nMasukkan Kode : ")
    if pilihan == "1":
        if bilik_tersedia: 
            bilik = bilik_tersedia.pop(0)  
            bilik_terpakai.append(bilik)
            print(f"> Bilik {bilik} sekarang terpakai.")
        else:
            print("> Semua bilik sudah terpakai!")

    elif pilihan == "2":
        if bilik_terpakai:
            bilik = bilik_terpakai.pop(0)   
            bilik_tersedia.append(bilik)
            bilik_tersedia.sort()
            print(f"> Bilik {bilik} sekarang tersedia kembali.")
        else:
            print("> Tidak ada bilik yang sedang terpakai!")

    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi")

    print(" ")