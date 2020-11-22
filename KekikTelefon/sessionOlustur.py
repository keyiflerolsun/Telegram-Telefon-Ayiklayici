# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded
from time import sleep
import os, json

SESSION  = 'sessionlar/'
if not os.path.isdir(SESSION):
    os.mkdir(SESSION)

def sessioncu():
    api_id    = input('API ID: ')
    api_hash  = input('API HASH: ')
    telefon   = input('Telefon Numarası (+90 ile): ')
    print('\n')

    try:
        client = Client(f'{SESSION}{telefon}', api_id, api_hash)
        client.connect()
        kod    = client.send_code(telefon)
        try:
            giris_yap = client.sign_in(telefon, kod.phone_code_hash, input('Doğrulama Kodu: '))
            client.accept_terms_of_service(str(giris_yap.id))
        except AssertionError:
            sleep(5)
        except SessionPasswordNeeded:
            client.check_password(input(f'İki Adımlı Doğrulama Şifresi ({client.get_password_hint()}): '))
        client.disconnect()
    except Exception as hata:
        os.remove(f'{SESSION}{telefon}.session')
        print(f'Hata Var !\n\t`{type(hata).__name__}`\n\t{hata}')
        return

    with client as app:
        app.send_message('me', f'__Merhaba, Ben **KekikTelefon** Tarafından Gönderildim!__\n\n__Senin Bilgilerin;__\n\n**ID :** `{api_id}`\n**Hash :** `{api_hash}`\n**Telefon :** `{telefon}`\n\n**Kendi gizliliğin için bunları kimseyle paylaşma..**')

    dict2json({
            'id'    : api_id,
            'hash'  : api_hash,
            'tel'   : telefon
        }, dosya_adi=f'{SESSION}bilgiler.json')

    print(f'\n\n\t\t{telefon} Session Kayıt Edildi..!')

def dict2json(sozluk:dict, dosya_adi:str):
    if os.path.isfile(dosya_adi):
        with open(dosya_adi) as gelen_json:
            gelen_veri = json.load(gelen_json)

        gelen_veri.append(sozluk)

        with open(dosya_adi, mode='w') as dosya:
            dosya.write(json.dumps(gelen_veri, indent=2, ensure_ascii=False, sort_keys=False))

    else:
        with open(dosya_adi, mode='w') as dosya:
            liste = [sozluk]
            essiz = [dict(sozluk) for sozluk in {tuple(liste_ici.items()) for liste_ici in liste}]
            a_z   = sorted(essiz, key=lambda sozluk: sozluk['id'])
            dosya.write(json.dumps(a_z, indent=2, ensure_ascii=False, sort_keys=False))