# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from konsolTaban._evrensel.tanimlar import kullanici_adi, bellenim_surumu, isletim_sistemi
from konsolTaban._degiskenler.banner import pencere_basligi, bildirim_metni
from konsolTaban._evrensel.pencere_basligi import win_baslik
import platform, os

def bildirim():
    if platform.machine() == "aarch64":
        return
    elif kullanici_adi == "gitpod":
        return
    elif bellenim_surumu.split('-')[-1] == 'aws':
        return
    elif isletim_sistemi == "Windows" and bellenim_surumu >= "10":
        try:
            from win10toast import ToastNotifier
        except ModuleNotFoundError:
            os.system('pip install win10toast')
            from win10toast import ToastNotifier


        win_baslik()
        bildirim = ToastNotifier()
        bildirim.show_toast(f"{pencere_basligi}", f"{bildirim_metni}",
            icon_path=None, duration=10, threaded=True
            )
    elif isletim_sistemi == "Linux":
        try:
            import notify2
        except ModuleNotFoundError:
            os.system('pip install notify2')
            import notify2

        notify2.init(pencere_basligi)
        bildirim = notify2.Notification(f"{pencere_basligi}", f"{bildirim_metni}", "notification-message-im")
        bildirim.show()

bildirim()