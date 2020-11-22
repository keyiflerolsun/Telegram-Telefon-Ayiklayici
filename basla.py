# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from konsolTaban._renkler.gokkusagi import yesil, sari, cyan, kirmizi, l_mavi
from konsolTaban._evrensel.tanimlar import ust_bilgi, isletim_sistemi, oturum, temizle
from konsolTaban._degiskenler.banner import logo

from os import getcwd
from time import sleep

from KekikTelefon import sessioncu, ayiklayici

def acilis_sayfasi():
    temizle()
    print(yesil + logo)
    print(ust_bilgi)
    print(f"""
    {yesil}[{sari} 1 {yesil}] {cyan}Session Oluştur
    {yesil}[{sari} 2 {yesil}] {cyan}Sessionların Dahil Olduğu Gruplardan Telefon Numarası Dızla
    """)

    konum = getcwd()
    konum = konum.split("\\") if isletim_sistemi == "Windows" else konum.split("/")
    secenek = str(input(f"{kirmizi}{oturum}:{l_mavi}~/../{konum[-2] + '/' + konum[-1]} >> {yesil}"))

    #-----------------------#
    if secenek == '1':
        temizle()
        print(l_mavi + logo)
        print(ust_bilgi)


        sessioncu()
        sleep(2)
        # acilis_sayfasi()
    #-----------------------#
    elif secenek == '2':
        temizle()
        print(l_mavi + logo)
        print(ust_bilgi)


        ayiklayici()
        # sleep(2)
        # acilis_sayfasi()
    #-----------------------#
    elif secenek.lower() == 'q':
        import sys
        sys.exit()
    #-----------------------#
    else:
        temizle()
        acilis_sayfasi()


if __name__ == '__main__':
    acilis_sayfasi()