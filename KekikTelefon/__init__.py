# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikTelefon.sessionOlustur import sessioncu
from KekikTelefon.DIZ import ayiklayici

from KekikTaban import KekikTaban

taban = KekikTaban(
    baslik   = "@KekikAkademi TelefonScript",
    aciklama = "KekikTelefon Başlatıldı..",
    banner   = "KekikTelefon",
    girinti  = 3
)

konsol = taban.konsol