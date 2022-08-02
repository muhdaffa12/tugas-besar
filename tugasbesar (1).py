def login():
    print("""
    ----------------------------------------------------
    SELAMAT DATANG DI TRAVEL SURABAYA
    TEMPAT BERBAGAI MACAM TEMPAT BERMAIN DISEKITAR SURABAYA
    ----------------------------------------------------
    silahkan masukkan user dan password
    user admin
    pass admin
    """)
    user=input("Masukkan username :")
    password=input("Masukkan password :")
    if user=="admin" and password=="admin":
        def menu():
            print("""
    ----------------------------------------------------
    SELAMAT DATANG DI TRAVEL SURABAYA
    TEMPAT BERBAGAI MACAM TEMPAT BERMAIN DISEKITAR SURABAYA
    ----------------------------------------------------
    silahkan masukan pilihan yang diinginkan

    a. Pesan Tiket Masuk Genjeran
    b. Pesan Tiket Masuk Kebun binatang Surabaya
    c. Pesan Tiket Masuk Museum 10 November
    d. Mengurutkan Data Pembeli
    e. Log Out
    f. Keluar Aplikasi
    ----------------------------------------------------
    HARAP UNTUK MENUTUP APLIKASI SETELAH MENCETAK TIKET
    ----------------------------------------------------
                     TERIMA KASIH
                """)
            pilihtiket = input("Silahkan pilih pembelian tiket dengan memasukkan abjad dari list di atas :")
            if pilihtiket == "a" or pilihtiket == "A":
                def kenjeran():
                    print("""
    ------------------------------------
    TIKET MASUK GENJERAN
    ------------------------------------
    a. Tiket Naik Perahu        Rp 20000
    b. Tiket Banana Boats       Rp 40000
    c. Tiket Speed Boats        Rp 70000
    d. Kembali ke menu awal

    ------------------------------------                    
                        """)
                    pilihan = input("Silahkan pilih tiket genjeran dengan memasukkan abjad dari list diatas :")
                    if pilihan == "a" or pilihan == "A":
                        from datetime import datetime
                        current = datetime.now()
                        tahun = current.year
                        bulan = current.month
                        hari = current.day
                        jumlahorang = int(input("Jumlah orang :"))
                        if jumlahorang > 4:
                            print("Jumlah maksimal untuk satu tiket 4 orang")
                            kenjeran()
                        if jumlahorang < 4:
                            hargatiketorang = 20000
                        totalharga = hargatiketorang * jumlahorang
                        print("Total yang harus dibayar : Rp", totalharga)
                        jumlahbayar = int(input("Uang yang diterima :"))
                        nama = []
                        umur = []
                        for i in range(jumlahorang):
                            print("\nData ke-", i + 1)
                            nama_pengunjung = input("Masukkan nama :")
                            nama.append(nama_pengunjung)
                            umur_pengunjung = int(input("Masukkan umur :"))
                            umur.append(umur_pengunjung)
                        for i in range(jumlahorang):
                            if umur[i] <= 9:
                                pendamping = input("Masukkan nama pendamping :")
                                kontak = input("Masukkan kontak pendamping :")
                            else:
                                pendamping = "-"
                                kontak = "-"
                        for i in range(jumlahorang):
                            perbaruikenjeran1=input('''
Apakah anda ingin mengubah data pesanan?
1. Jika ingin mengubah
2. Jika tidak ingin mengubah
Silahkan Masukan pilihan anda : ''')
                            if perbaruikenjeran1 == '1':
                                kenjeran()
                            elif perbaruikenjeran1 == '2':
                                print("----------------------------------------------")
                                print("Tiket Orang Masuk Genjeran")
                                print("----------------------------------------------")
                                print("{}/{}/{}".format(hari, bulan, tahun))
                                print("pendamping :", pendamping)
                                print("kontak :", kontak)
                                for cetaknama in nama:
                                    print("nama : {}".format(cetaknama))
                                for cetakumur in umur:
                                    f=open('pesanan.txt', 'a')
                                    f.write('\n')
                                    f.write('Tiket Naik Perahu')
                                    f.write(', ')
                                    f.writelines(str(nama))
                                    f.write(', Umur ')
                                    f.writelines(str(umur))
                                    f.close()
                                    print("umur : {}".format(cetakumur))
                                    print("----------------------------------------------")
                                    print("Harga : Rp", hargatiketorang)
                                    print("Total Harga : Rp", totalharga)
                                    print("Kembali : Rp", jumlahbayar - totalharga)
                                    print("----------------------------------------------")
                                    print("Terimakasih")
                                    print("----------------------------------------------")
                                    menu()
                    elif pilihan == 'b' or pilihan == 'B':
                        from datetime import datetime
                        current = datetime.now()
                        tahun = current.year
                        bulan = current.month
                        hari = current.day
                        jumlahorang = int(input("Jumlah orang :"))
                        if jumlahorang > 6:
                            print("Jumlah maksimal untuk satu tiket 4 orang")
                            kenjeran()
                        if jumlahorang < 6:
                            hargatiketorang = 40000
                        totalharga = hargatiketorang * jumlahorang
                        print("Total yang harus dibayar : Rp", totalharga)
                        jumlahbayar = int(input("Uang yang diterima :"))
                        nama = []
                        umur = []
                        for i in range(jumlahorang):
                            print("\ndata ke-", i + 1)
                            nama_pengunjung = input("masukan nama :")
                            nama.append(nama_pengunjung)
                            umur_pengunjung = int(input("masukan umur :"))
                            umur.append(umur_pengunjung)
                        for i in range(jumlahorang):
                            if umur[i] <= 15:
                                pendamping = input("masukan nama pendamping")
                                kontak = input("masukan kontak pendamping")
                            else:
                                pendamping = "-"
                                kontak = "-"
                            for i in range(jumlahorang):
                                perbaruikenjeran1=input('''
Apakah anda ingin mengubah data pesanan?
1. Jika ingin mengubah
2. Jika tidak ingin mengubah
Silahkan Masukan pilihan anda : ''')
                                if perbaruikenjeran1 == '1':
                                    kenjeran()
                                elif perbaruikenjeran1 == '2':
                                    print("-----------------------------------")
                                    print("Tiket orang masuk Genjeran")
                                    print("-----------------------------------")
                                    print("{}/{}/{}".format(hari, bulan, tahun))
                                    print("pendamping :", pendamping)
                                    print("kontak:", kontak)
                                    f=open('pesanan.txt', 'a')
                                    f.write('\n')
                                    f.write('Tiket Banana Boats')
                                    f.write(', ')
                                    f.writelines(str(nama))
                                    f.write(', Umur ')
                                    f.writelines(str(umur))
                                    f.close()
                                    for cetaknama in nama:
                                        print("nama : {}".format(cetaknama))
                                    for cetakumur in umur:
                                        print("umur : {}".format(cetakumur))
                                        print("------------------------------------")
                                        print("Harga : Rp", hargatiketorang)
                                        print("Kembali : Rp", jumlahbayar - totalharga)
                                        print("-------------------------------------")
                                        print("TerimaKasih")
                                        menu()
                    elif pilihan == 'c' or pilihan == 'C':
                        from datetime import datetime
                        current = datetime.now()
                        tahun = current.year
                        bulan = current.month
                        hari = current.day
                        jumlahorang = int(input("Jumlah orang :"))
                        if jumlahorang > 2:
                            print("Jumlah maksimal untuk satu tiket 4 orang")
                            kenjeran()
                        if jumlahorang < 2:
                            hargatiketorang = 70000
                        totalharga = hargatiketorang * jumlahorang
                        print("Total yang harus dibayar : Rp", totalharga)
                        jumlahbayar = int(input("Uang yang diterima :"))
                        nama = []
                        umur = []
                        for i in range(jumlahorang):
                            print("\ndata ke-", i + 1)
                            nama_pengunjung = input("masukan nama :")
                            nama.append(nama_pengunjung)
                            umur_pengunjung = int(input("masukan umur :"))
                            umur.append(umur_pengunjung)
                        for i in range(jumlahorang):
                            if umur[i] <= 0:
                                pendamping = input("masukan nama pendamping")
                                kontak = input("masukan kontak pendamping")
                            else:
                                pendamping = "-"
                                kontak = "-"
                            for i in range(jumlahorang):
                                perbaruikenjeran1=input('''
Apakah anda ingin mengubah data pesanan?
1. Jika ingin mengubah
2. Jika tidak ingin mengubah
Silahkan Masukan pilihan anda : ''')
                                if perbaruikenjeran1 == '1':
                                    kenjeran()
                                elif perbaruikenjeran1 == '2':
                                    print("-----------------------------------")
                                    print("Tiket orang masuk Genjeran")
                                    print("-----------------------------------")
                                    print("{}/{}/{}".format(hari, bulan, tahun))
                                    print("pendamping :", pendamping)
                                    print("kontak:", kontak)
                                    f=open('pesanan.txt', 'a')
                                    f.write('\n')
                                    f.write('Tiket Speed Boats')
                                    f.write(', ')
                                    f.writelines(str(nama))
                                    f.write(', Umur ')
                                    f.writelines(str(umur))
                                    f.close()
                                    for cetaknama in nama:
                                        print("nama : {}".format(cetaknama))
                                    for cetakumur in umur:
                                        print("umur : {}".format(cetakumur))
                                        print("------------------------------------")
                                        print("Harga : Rp", hargatiketorang)
                                        print("Kembali : Rp", jumlahbayar - totalharga)
                                        print("-------------------------------------")
                                        print("TerimaKasih")
                                        menu()
                    elif pilihan == 'd' or pilihan == 'D':
                        menu()
                    else:
                        print('Pilihan salah! menutup aplikasi')
                        quit()
                kenjeran()
            elif pilihtiket == 'b' or pilihtiket == 'B':
                def kbs():
                    import time
                    hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu")
                    sekarang = time.time()
                    infowaktu = time.localtime(sekarang)
                    info_hari = hari[infowaktu[6]]
                    print('''
    --------------------------------------------------
    TIKET MASUK KEBUN BINATANG SURABAYA
    --------------------------------------------------
    Tiket Kebun Binatang   Rp 160.000
    *Pembelian tiket standard untuk satu 
    atau dua orang 
    ------------------------------------
    Discount Tiket Kebun Binatang    Rp 100.000
    *Di minimal pembelian 3 tiket
    ---------------------------------------------------
                        ''')
                    lanjut=input("masukkan 1 untuk lanjut 2 untuk kembali ke menu awal :")
                    if lanjut == '1':
                        from datetime import datetime
                        current = datetime.now()
                        tahun = current.year
                        bulan = current.month
                        hari = current.day
                        jumlahorang = int(input("Jumlah orang :"))
                        if jumlahorang > 3:
                            print("Jumlah maksimal pesan 3 orang")
                        hargatiketkbs = 160000
                        if jumlahorang == 3:
                            hargatiketkbs = 100000
                        totalharga = hargatiketkbs * jumlahorang
                        print("Total yang harus dibayar : Rp", totalharga)
                        jumlahbayar = int(input("Uang yang diterima :"))
                        nama = []
                        umur = []
                        for i in range(jumlahorang):
                            print("\nData ke-", i + 1)
                            nama_pengunjung = input("Masukkan nama :")
                            nama.append(nama_pengunjung)
                            umur_pengunjung = int(input("Masukkan umur :"))
                            umur.append(umur_pengunjung)
                        for i in range(jumlahorang):
                            if umur[i] <= 9:
                                pendamping = input("Masukkan nama pendamping :")
                                kontak = input("Masukkan kontak pendamping :")
                                break
                            else:
                                pendamping = "-"
                                kontak = "-"
                        for i in range(jumlahorang):
                            perbaruikbs=input('''
Apakah anda ingin mengubah data pesanan?
1. Jika ingin mengubah
2. Jika tidak ingin mengubah
Silahkan Masukan pilihan anda : ''')
                            if perbaruikbs == '1':
                                kbs()
                            elif perbaruikbs == '2':
                                print("----------------------------------------------")
                                print("Tiket Masuk Kebun Binatang Surabaya")
                                print("----------------------------------------------")
                                print(info_hari,"{}/{}/{}".format(hari, bulan, tahun))
                                print("pendamping :", pendamping)
                                print("kontak :", kontak)
                            for cetaknama in nama:
                                print("nama : {}".format(cetaknama))
                            for cetakumur in umur:
                                f=open('pesanan.txt', 'a')
                                f.write('\n')
                                f.write('Tiket Kebun Binatang Surabaya')
                                f.write(', ')
                                f.writelines(str(nama))
                                f.write(', Umur ')
                                f.writelines(str(umur))
                                f.close()
                                print("umur : {}".format(cetakumur))
                                print("----------------------------------------------")
                                print("Harga : Rp", hargatiketkbs)
                                print("Total Harga : Rp", totalharga)
                                print("Kembali : Rp", jumlahbayar - totalharga)
                                print("----------------------------------------------")
                                print("Terimakasih")
                                print("----------------------------------------------")
                                menu()
                    elif lanjut == '2':
                        menu()
                kbs()
            elif pilihtiket == 'c' or pilihtiket == 'C':
                def museum():
                    import time
                    hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu")
                    sekarang = time.time()
                    infowaktu = time.localtime(sekarang)
                    info_hari = hari[infowaktu[6]]
                    print('''
    -----------------------------------------------------------
    TIKET MASUK Musium 10 November
    -----------------------------------------------------------
    Tiket Masuk Musium 10 November   Rp 120.000
    *Pembelian tiket standard untuk satu 
    atau dua orang 
    -----------------------------------------------------------
    Discount Tiket Musium 10 November     Rp 65.000
    *Di minimal pembelian 3 tiket
    -----------------------------------------------------------
                        ''')
                    lanjut=input("masukkan 1 untuk lanjut 2 untuk kembali ke menu awal :")
                    if lanjut == '1':
                        from datetime import datetime
                        current = datetime.now()
                        tahun = current.year
                        bulan = current.month
                        hari = current.day
                        jumlahorang = int(input("Jumlah orang :"))
                        if jumlahorang > 3:
                            print("Jumlah maksimal pesan 3 orang")
                        hargatiketmusium = 120000
                        if jumlahorang == 3:
                            hargatiketmusium = 65000
                        totalharga = hargatiketmusium * jumlahorang
                        print("Total yang harus dibayar : Rp", totalharga)
                        jumlahbayar = int(input("Uang yang diterima :"))
                        nama = []
                        umur = []
                        for i in range(jumlahorang):
                            print("\nData ke-", i + 1)
                            nama_pengunjung = input("Masukkan nama :")
                            nama.append(nama_pengunjung)
                            umur_pengunjung = int(input("Masukkan umur :"))
                            umur.append(umur_pengunjung)
                        for i in range(jumlahorang):
                            if umur[i] <= 9:
                                pendamping = input("Masukkan nama pendamping :")
                                kontak = input("Masukkan kontak pendamping :")
                            else:
                                pendamping = "-"
                                kontak = "-"
                        for i in range(jumlahorang):
                            perbaruimuseum=input('''
Apakah anda ingin mengubah data pesanan?
1. Jika ingin mengubah
2. Jika tidak ingin mengubah
Silahkan Masukan pilihan anda : ''')
                            if perbaruimuseum == '1':
                                museum()
                            elif perbaruimuseum == '2':
                                print("----------------------------------------------")
                                print("Tiket Masuk Musium 10 November")
                                print("----------------------------------------------")
                                print(info_hari,"{}/{}/{}".format(hari, bulan, tahun))
                                print("pendamping :", pendamping)
                                print("kontak :", kontak)
                            for cetaknama in nama:
                                print("nama : {}".format(cetaknama))
                            for cetakumur in umur:
                                f=open('pesanan.txt', 'a')
                                f.write('\n')
                                f.write('Tiket Museum 10 November')
                                f.write(', ')
                                f.writelines(str(nama))
                                f.write(', Umur ')
                                f.writelines(str(umur))
                                f.close()
                                print("umur : {}".format(cetakumur))
                                print("----------------------------------------------")
                                print("Harga : Rp", hargatiketmusium)
                                print("Total Harga : Rp", totalharga)
                                print("Kembali : Rp", jumlahbayar - totalharga)
                                print("----------------------------------------------")
                                print("Terimakasih")
                                print("----------------------------------------------")
                                menu()
                    if lanjut == '2':
                        menu()
                museum()
            elif pilihtiket == 'd' or pilihtiket == 'D':
                def urutkan():
                    def sorting(filename):
                        infile = open(filename)
                        words = []
                        for line in infile:
                            temp = line.split('\n')
                            for i in temp:
                                words.append(i)
                        infile.close()
                        words.sort()
                        print('data telah di urutkan')
                        print(words)
                    sorting("pesanan.txt")
                    menu()
                urutkan()
            elif pilihtiket == 'e' or pilihtiket == 'E':
                login()
            elif pilihtiket == 'f' or pilihtiket == 'F':
                quit()
            else:
                print('Pilihan Salah! Kembali ke menu login')
                login()
        menu()
login()
