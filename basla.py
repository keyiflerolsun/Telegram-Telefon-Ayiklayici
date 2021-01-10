# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import asyncio
from KekikTelefon import konsol, taban, sessioncu, ayiklayici
from os import getcwd
from time import sleep

def acilis_sayfasi():
    taban.logo_yazdir('green')
    taban.bilgi_yazdir()

    konsol.print(f"""
    [bold green][[/] [bold yellow]1[/] [bold green]][/] [bold cyan]Session Oluştur[/]
    [bold green][[/] [bold yellow]2[/] [bold green]][/] [bold cyan]Sessionların Dahil Olduğu Gruplardan Telefon Numarası Dızla[/]
    """) # Seçeneklerimizi ayarladık

    konum = getcwd()
    if taban.isletim_sistemi == "Windows":
        konum = konum.split("\\")
    else:
        konum = konum.split("/")

    # Kullanıcı için input oluşturalım..
    secenek = str(konsol.input(f"[red]{taban.oturum}[/][bright_blue]:~/../{konum[-2] + '/' + konum[-1]}[/] [bold green]>>[/] "))
    #-----------------------#
    if secenek == '1':
        taban.logo_yazdir()
        taban.bilgi_yazdir()

        asyncio.run(sessioncu())
        # sleep(2)
        # acilis_sayfasi()
    #-----------------------#
    elif secenek == '2':
        taban.logo_yazdir()
        taban.bilgi_yazdir()

        asyncio.run(ayiklayici())
        # sleep(2)
        # acilis_sayfasi()
    #-----------------------#
    elif secenek.lower() == 'q':
        import sys
        sys.exit()
    #-----------------------#
    else:
        acilis_sayfasi()


if __name__ == '__main__':
    acilis_sayfasi()