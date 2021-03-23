# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded
from time import sleep
import os, json

SESSION  = 'sessionlar/'
if not os.path.isdir(SESSION):
    os.mkdir(SESSION)

async def sessioncu():
    api_id    = input('API ID        : ')
    api_hash  = input('API HASH      : ')
    telefon   = input('Telefon(+xxxx): ').replace(' ', '')
    print('\n')

    try:
        client = Client(f'{SESSION}{telefon}', api_id, api_hash)
        await client.connect()
        kod    = await client.send_code(telefon)
        try:
            giris_yap = await client.sign_in(telefon, kod.phone_code_hash, input('Doğrulama Kodu: '))
            await client.accept_terms_of_service(str(giris_yap.id))
        except AssertionError:
            sleep(5)
        except SessionPasswordNeeded:
            await client.check_password(input(f'İki Adımlı Doğrulama Şifresi ({await client.get_password_hint()}): '))
        await client.disconnect()
    except Exception as hata:
        os.remove(f'{SESSION}{telefon}.session')
        print(f'Hata Var !\n\t`{type(hata).__name__}`\n\t{hata}')
        return

    bilgilerim = {}
    async with client as app:
        ben = await app.get_me()
        bilgilerim['nick'] = f"@{ben.username}" if ben.username else None
        bilgilerim['ad']   = f"{ben.first_name or ''} {ben.last_name or ''}".strip()
        bilgilerim['uid']  = ben.id

        await app.send_message('me', f'__Merhaba, Ben **KekikTelefon** Tarafından Gönderildim!__\n\n__Senin Bilgilerin;__\n\n**ID :** `{api_id}`\n**Hash :** `{api_hash}`\n**Telefon :** `{telefon}`\n\n**Kendi gizliliğin için bunları kimseyle paylaşma..**')

    await dict2json({
            'api_id'        : api_id,
            'api_hash'      : api_hash,
            'telefon'       : telefon,
            'kullanici_id'  : bilgilerim['uid'],
            'kullanici_nick': bilgilerim['nick'],
            'kullanici_adi' : bilgilerim['ad']
        }, dosya_adi=f'{SESSION}bilgiler.json')

    print(f'\n\n\t\t{telefon} Session Kayıt Edildi..!')

async def dict2json(sozluk:dict, dosya_adi:str):
    if os.path.isfile(dosya_adi):
        with open(dosya_adi, encoding='utf-8') as gelen_json:
            gelen_veri = json.load(gelen_json)

        gelen_veri.append(sozluk)

        with open(dosya_adi, mode='w', encoding='utf-8') as dosya:
            dosya.write(json.dumps(gelen_veri, indent=2, ensure_ascii=False, sort_keys=False))

    else:
        with open(dosya_adi, mode='w', encoding='utf-8') as dosya:
            liste = [sozluk]
            essiz = [dict(sozluk) for sozluk in {tuple(liste_ici.items()) for liste_ici in liste}]
            a_z   = sorted(essiz, key=lambda sozluk: sozluk['api_id'])
            dosya.write(json.dumps(a_z, indent=2, ensure_ascii=False, sort_keys=False))