# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:43:11 2021

@author Yulia widya 2E
UAS algoritma pemrograman 
"""

import datetime


x = datetime.datetime.now()

print("_____________________________________________")

print("______PERHITUNGAN GAJI KARYAWAN CV.LOGOS_____")

print("             Tanggal : ",x.strftime("%x"))

print("______________________________________________")


golongan = ['1','2','3']
gajipokok = ['2500000','4500000','6500000']

nama = input("Nama                    =       ")
g= input("Golongan                =       ")
gol = int(g)
if gol == 1 :
    idx = 0
    tunjangan = 0.01
elif gol == 2:
    idx = 1
    tunjangan = 0.03
elif gol == 3:
    idx = 2
    tunjangan = 0.05
else :
    print("Masukkan kembali golongan dengan benar")

print("Laki - Laki atau Perempuan")
jenis_kelamin = input("Jenis kelamin           =      ")
print ("Kawin atau belum")
status_kawin = input("status Kawin            =      ")
status_anak = input("Apakah punya anak       =      ")

#istri
if jenis_kelamin == "Laki Laki" or "Laki laki" or "laki laki" and status_kawin == "Kawin" or "kawin":
   tunjanganistri = int(gajipokok[idx]) * tunjangan
else :
    tunjanganistri = 0
#Anak
if status_kawin == "Kawin" or "kawin" and status_anak == "Iya" or "iya":
    tunjangananak = int(gajipokok[idx]) * 0.02
else :
    tunjangananak = 0
#Bruto
gajibruto = int(gajipokok[idx]) + int(tunjanganistri) + int(tunjangananak)

#Jabatan
biayajabatan = int(gajibruto) * 0.05

#Pensiun
iuran_pensiun = 15500

#Organsasi
iuran_organisasi = 3500

#Net
GajiNetto = int(gajibruto) - int(iuran_organisasi) - int(iuran_pensiun)
 


    

    


print("____________________________________________________")
print("                         SLIP GAJI                   ")
print("              Tanggal : ",x.strftime("%x"))
print("____________________________________________________")
print("Nama                     " + nama)
print("Golongan                 " + str(gol))
print("jenis kelamin            " + jenis_kelamin)
print("Staus Kawin              " + status_kawin)
print("Gaji Pokok               " + gajipokok[idx])
print("Tunjangan istri          " + str(tunjanganistri))
print("Tunjangan Anak           " + str(tunjangananak))
print(">>Gaji bruto             " + str(gajibruto))
print("______________________________________________________")
print("Biaya Jabatan            " + str(biayajabatan))
print("Iuran Pensiun            " + str(iuran_pensiun))
print("Iuran Organisasi         " + str(iuran_organisasi))
print(">>Gaji Netto             " + str(GajiNetto))