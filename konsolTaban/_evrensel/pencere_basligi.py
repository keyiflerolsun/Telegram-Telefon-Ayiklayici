# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from konsolTaban._evrensel.tanimlar import isletim_sistemi
from konsolTaban._degiskenler.banner import pencere_basligi
import os

def win_baslik():
    if isletim_sistemi == "Windows":
        try:
            import ctypes
        except ModuleNotFoundError:
            os.system('pip install ctypes')
            import ctypes

        ctypes.windll.kernel32.SetConsoleTitleW(f"{pencere_basligi}")