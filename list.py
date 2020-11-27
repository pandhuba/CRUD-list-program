# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:05:43 2020

@author: Tulenesia
"""

class list:
    def crud(menu):
        
        global mhs
        
        if menu == 1:
            print("\nData Mahasiswa Yang Sudah Masuk : \n", mhs)
            list.list()
            
        elif menu == 2:
            jmlh_rows = int(input("Masukkan jumlah mahasiswa : "))
            jmlh_cols = 1
            mhs = []
        
            for i in range(jmlh_rows):
                inner = []
                for j in range(jmlh_cols):
                    i += 1
                    no = i
                    nama = input("Masukkan nama mahasiswa ke-%d \t\t: " %i)
                    nim = input("Masukkan nim mahasiswa ke-%d \t\t: " %i)
                    jurusan = input("Masukkan jurusan mahasiswa ke-%d \t: " %i)
                    kota = input("Masukkan kota mahasiswa ke-%d \t\t: " %i)
                    
                    inner.append(no)
                    inner.append(nama)
                    inner.append(nim)
                    inner.append(jurusan)
                    inner.append(kota)
                
                mhs.append(inner)
            
            print("\nData Mahasiswa Yang Sudah Masuk : \n", mhs)
            list.list()
            
        elif menu == 3:
            while True:
                print("\nData Mahasiswa Yang Sudah Masuk : \n", mhs)
                no = int(input("Update data mahasiswa no : "))
                no = no-1
                print(mhs[no])
                print("1. Edit nama")
                print("2. Edit nim")
                print("3. Edit jurusan")
                print("4. Edit kota")
                print("5. Kembali")
                menuUpdate = int(input("Pilih (1/2/3/4/5) : "))
                
                if menuUpdate == 1:
                    print("Nama lama \t: ", mhs[no][1])
                    namaBaru = input("Nama baru \t\t: ")
                    mhs[no][1] = namaBaru
                    print(mhs[no])
                    pilih = str(input("Ingin update lagi? (y/n) : "))
                    if pilih == 'y':
                        True
                    elif pilih == 'n':
                        list.list()
                    else:
                        print("Masukkan Salah!")
                        break
                
                elif menuUpdate == 2:
                    print("Nim lama \t: ", mhs[no][2])
                    nimBaru = input("Nim baru \t\t: ")
                    mhs[no][2] = nimBaru
                    print(mhs[no])
                    pilih = str(input("Ingin update lagi? (y/n) : "))
                    if pilih == 'y':
                        True
                    elif pilih == 'n':
                        list.list()
                    else:
                        print("Masukkan Salah!")
                        break
                    
                elif menuUpdate == 3:
                    print("Jurusan lama \t: ", mhs[no][3])
                    jurusanBaru = input("Jurusan baru \t: ")
                    mhs[no][3] = jurusanBaru
                    print(mhs[no])
                    pilih = str(input("Ingin update lagi? (y/n) : "))
                    if pilih == 'y':
                        True
                    elif pilih == 'n':
                        list.list()
                    else:
                        print("Masukkan Salah!")
                        break
                    
                elif menuUpdate == 4:
                    print("Kota lama \t: ", mhs[no][4])
                    kotaBaru = input("Kota baru \t\t: ")
                    mhs[no][4] = kotaBaru
                    print(mhs[no])
                    pilih = str(input("Ingin update lagi? (y/n) : "))
                    if pilih == 'y':
                        True
                    elif pilih == 'n':
                        list.list()
                    else:
                        print("Masukkan Salah!")
                        break
                
                elif menuUpdate == 5:
                    list.list()
                    
                else:
                    print("Menu salah!")
                    True
                    
        elif menu == 4:
            print("\nData Mahasiswa Yang Sudah Masuk : \n", mhs)
            no = int(input("Hapus data mahasiswa no : "))
            no = no-1
            del mhs[no]
            no = no+1
            print("Data mahasiswa no. %d sudah terhapus!" %no)
            list.list()
        
        elif menu == 5:
            quit()
        
        else:
            print("Menu yang dimasukkan salah!")
            quit()
                
    def list():
        print("\n")
        print("############# PANDHU BRIAN ALDHIANSYAH #############")
        print("----------------------------------------------------")
        print("======= Pengisian Data Mahasiswa Dengan List =======")
        print("1. Lihat Data Mahasiswa (Tambah data dulu)")
        print("2. Tambah Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")
        menu = int(input("Pilih menu (1/2/3/4/5) : "))
        list.crud(menu)
        
if __name__=="__main__":
    list.list()
    