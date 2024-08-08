from django.db import models


class DistrictChoices(models.IntegerChoices):
    # Andijon districts
    ANDIJON = 1, 'Andijon'
    ASAKA = 2, 'Asaka'
    BALIQCHI = 3, 'Baliqchi'
    BOZORARIK = 4, 'Bozorarik'
    BULUNGUR = 5, 'Bulung‘ur'
    JALAQUDIQ = 6, 'Jalaquduq'
    MARHAMAT = 7, 'Marhamat'
    OLOT = 8, 'Olot'
    PAHTAABAD = 9, 'Paxtaobod'
    XONABAD = 10, 'Xonabad'
    XONQA = 11, 'Xonqa'
    SHAHRIKHON = 12, 'Shahrikhon'
    SHURABAD = 13, 'Shurabad'

    # Buxoro districts
    BUXORO = 14, 'Buxoro'
    GIJDUVON = 15, 'G‘ijduvon'
    KOGON = 16, 'Kogon'
    KARMANA = 17, 'Karmana'
    VOBKENT = 18, 'Vobkent'
    BUKHARA = 19, 'Bukhara'
    GIZDUVON = 20, 'Gizduvon'

    # Farg‘ona districts
    FARGONA = 21, 'Farg‘ona'
    MARGILON = 22, 'Marg‘ilon'
    Qoqon = 23, 'Qo‘qon'
    RISHTON = 24, 'Rishton'
    TINCHLIK = 25, 'Tinchlik'
    URGANCHI = 26, 'Urganch'

    # Jizzax districts
    JIZZAX = 27, 'Jizzax'
    GALLAOROL = 28, 'G‘allaorol'
    YANGIYER2 = 29, 'Yangiyer'
    ZANGIOTA = 30, 'Zangiota'
    CHIRCHIK = 31, 'Chirchiq'

    # Xorazm districts
    XIVA = 32, 'Xiva'
    URGANCH = 33, 'Urganch'
    SHAVAT = 34, 'Shavat'
    KHIVA = 35, 'Khiva'

    # Namangan districts
    NAMANGAN = 36, 'Namangan'
    CHORTOQ = 37, 'Chortoq'
    MINGBULAK = 38, 'Mingbulak'
    UCHKOPRIK = 39, 'Uchko‘prik'

    # Navoiy districts
    NAVOIY = 40, 'Navoiy'
    ZARAFSHON = 41, 'Zarafshon'
    QIZILTEPA = 42, 'Qiziltepa'

    # Qashqadaryo districts
    QARSHI = 43, 'Qarshi'
    SHAKHRISABZ = 44, 'Shahrisabz'
    KITAB = 45, 'Kitab'

    # Samarqand districts
    SAMARQAND = 46, 'Samarqand'
    KATTASAY = 47, 'Kattasay'
    KATTALIK = 48, 'Kattalik'

    # Sirdaryo districts
    GULISTON = 49, 'Guliston'
    YANGIYER = 50, 'Yangiyer'

    # Surxondaryo districts
    TERMIZ = 51, 'Termiz'
    SHORCHI = 52, 'Sho‘rchi'

    # Toshkent districts
    TOSHkent = 53, 'Toshkent'
    CHIRCHIK2 = 54, 'Chirchiq'

    # Qoraqalpog‘iston Respublikasi districts
    NUKUS = 55, 'Nukus'
    BERUNIY = 56, 'Beruniy'
