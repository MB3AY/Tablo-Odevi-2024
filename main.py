import numpy as np
from prettytable import PrettyTable
from colorama import Fore, Style
# pandas kütüphanesi ile tabloyu düzgün çıkaramadım. bu sebeple araştırdım ve prettytable kullanmaya karar verdim.
# colorama kütüphanesi ile de tabloyu renklendirdim.

yas_dizisi = np.array([15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65])
c1 = 16
c2 = 22

def en_yakin_merkez(yas, kume_1, kume_2):
    k1_mesafe = abs(yas - kume_1)
    k2_mesafe = abs(yas - kume_2)
    en_yakin_kume = kume_1 if k1_mesafe <= k2_mesafe else kume_2
    return en_yakin_kume

def kume_bul(kume1, kume2):
    k1_toplam = 0
    k2_toplam = 0
    k1_elemanlar = 0
    k2_elemanlar = 0

    for yas in yas_dizisi:
        en_yakin_kume = en_yakin_merkez(yas, kume1, kume2)
        if en_yakin_kume == kume2:
            k2_elemanlar += 1
            k2_toplam += yas
        elif en_yakin_kume == kume1:
            k1_elemanlar += 1
            k1_toplam += yas

    kume1_ortalama = k1_toplam / k1_elemanlar if k1_elemanlar != 0 else 0
    kume2_ortalama = k2_toplam / k2_elemanlar if k2_elemanlar != 0 else 0

    return {"kume1_ortalama": kume1_ortalama, "kume2_ortalama": kume2_ortalama}

son_c1 = c1
son_c2 = c2

for i in range(1, 5):
    kumeler = kume_bul(son_c1, son_c2)

    mesafe_1 = np.abs(yas_dizisi - son_c1)
    mesafe_2 = np.abs(yas_dizisi - son_c2)
    en_yakin_kume = np.where(mesafe_1 > mesafe_2, 2, 1)
    yeni_merkez = np.where(en_yakin_kume == 1, son_c1, son_c2)

    table = PrettyTable(["Xi", "C1", "C2", "Mesafe 1", "Mesafe 2", "En Yakın Kume", "Yeni Merkez"])
    for j in range(len(yas_dizisi)):
        if en_yakin_kume[j] == 1:
            table.add_row([Fore.GREEN + str(yas_dizisi[j]) + Style.RESET_ALL, son_c1, son_c2, mesafe_1[j], mesafe_2[j], en_yakin_kume[j], yeni_merkez[j]])
        elif en_yakin_kume[j] == 2:
            table.add_row([Fore.CYAN + str(yas_dizisi[j]) + Style.RESET_ALL, son_c1, son_c2, mesafe_1[j], mesafe_2[j], en_yakin_kume[j], yeni_merkez[j]])

    print(f"Iterasyon {i}:")
    print(table)
    print(f"Kume 1 Ortalama: {kumeler['kume1_ortalama']:.2f}, Kume 2 Ortalama: {kumeler['kume2_ortalama']:.2f}\n")

    son_c1 = kumeler['kume1_ortalama']
    son_c2 = kumeler['kume2_ortalama']
