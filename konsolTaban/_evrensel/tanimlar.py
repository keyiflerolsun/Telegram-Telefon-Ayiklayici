# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os, platform, requests, datetime, pytz
from konsolTaban._renkler.gokkusagi import l_siyah, l_kirmizi, l_yesil, sari

try:
    kullanici_adi = os.getlogin()
except OSError:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]

bilgisayar_adi = platform.node()
oturum = kullanici_adi + "@" + bilgisayar_adi                               # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()
bellenim_surumu = platform.release()
cihaz = isletim_sistemi + " | " + bellenim_surumu                          # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")
zaman = tarih + " | " + saat

ip = requests.get('https://api.ipify.org').text

ust_bilgi = f"\t\t{l_siyah}{kullanici_adi} {l_yesil}({ip})\n"
ust_bilgi += f"\t\t  {l_kirmizi}{cihaz}\n"
ust_bilgi += f"\t\t   {sari}{zaman}\n"

def temizle():
    if isletim_sistemi == "Windows":
        os.system("cls")
    else:
        os.system("clear")
temizle()