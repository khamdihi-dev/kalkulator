#!/usr/bin/python3
# coding=utf+8
# coded by KhamdihiDEV

import os, platform, sys

class main:

    def __init__(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        self.menu()

    def menu(self):
        print("""
  1. Penjumlahan
  2. Pengurangan
  3. Pembagian
  4. Perkalian\n""")
        xxx = input(" Pilih nomornya : ")
        if xxx in ['1','01']:self.jumlah()
        elif xxx in ['2','02']:self.kurang()
        elif xxx in ['3','03']:self.bagisaya()
        elif xxx in ['4','04']:self.kali()
        else:self.menu()

    # PENJUMLAHAN
    def jumlah(self):
        one = int(input("\n masukan angka pertama : "))
        two = int(input(" masukan angka kedua : "))
        res = one + two
        print(f'\n hasil dari {one} + {two} adalah : {res}')

    # PENGURANGAN
    def kurang(self):
        one = int(input("\n masukan angka pertama : "))
        two = int(input(" masukan angka kedua : "))
        res = one - two
        print(f'\n hasil dari {one} - {two} adalah : {res}')

    # PEMBAGIAN
    def bagisaya(self):
        one = int(input("\n masukan angka pertama : "))
        two = int(input(" masukan angka kedua : "))
        res = one / two
        print(f'\n hasil dari {one} / {two} adalah : {int(res)}')

    # PERKALIAN
    def kali(self):
        one = int(input("\n masukan angka pertama : "))
        two = int(input(" masukan angka kedua : "))
        res = one * two
        spl = str(res)
        print(f'\n hasil dari {one} * {two} adalah : {spl}')

if __name__ == '__main__':
   main()
