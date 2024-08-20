from django.db import models


class DistrictChoices(models.TextChoices):
    # SIRDARYO
    BOYOVUT = '1X1', 'BOYOVUT'
    GULISTON_SHAXRI = '1X2', 'GULISTON_SHAXRI'
    GULISTON = '1X3', 'GULISTON'
    OQOLTIN = '1X4', 'OQOLTIN'
    SARDOBA = '1X5', 'SARDOBA'
    SAYXUNOBOD = '1X6', 'SAYXUNOBOD'
    SHIRIN = '1X7', 'SHIRIN'
    SIRDARYO = '1X8', 'SIRDARYO'
    XOVOS = '1X9', 'XOVOS'
    YANGIYER = '1X10', 'YANGIYER'

    # NAVOI
    KARMANA = '2X1', 'KARMANA'
    KONIMEX = '2X2', 'KONIMEX'
    NAVBAHOR = '2X3', 'NAVBAHOR'
    NAVOIY = '2X4', 'NAVOIY'
    NUROTA = '2X5', 'NUROTA'
    QIZILTEPA = '2X6', 'QIZILTEPA'
    TOMDI = '2X7', 'TOMDI'
    UCHQUDUQ = '2X8', 'UCHQUDUQ'
    XATIRCHI = '2X9', 'XATIRCHI'
    ZARAFSHON = '2X10', 'ZARAFSHON'

    # JIZZAX
    ARNASOY = '3X1', 'ARNASOY'
    BAXMAL = '3X2', 'BAXMAL'
    DOSTLIK = '3X3', 'DOSTLIK'
    FORISH = '3X4', 'FORISH'
    GALLAOROL = '3X5', 'GALLAOROL'
    JIZZAX = '3X6', 'JIZZAX'
    JIZZAX_SHAXRI = '3X7', 'JIZZAX_SHAXRI'
    MIRZACHOL = '3X8', 'MIRZACHOL'
    PAXTAKOR = '3X9', 'PAXTAKOR'
    YANGIOBOD = '3X10', 'YANGIOBOD'
    ZAFAROBOD = '3X11', 'ZAFAROBOD'
    ZARBAND = '3X12', 'ZARBAND'
    ZOMIN = '3X13', 'ZOMIN'

    # XORAZM
    BOGOT = '4X1', 'BOGOT'
    GURLAN = '4X2', 'GURLAN'
    QOSHKOPIR = '4X3', 'QOSHKOPIR'
    SHOVOT = '4X4', 'SHOVOT'
    URGANCH_SHAHRI = '4X5', 'URGANCH_SHAHRI'
    URGANCH = '4X6', 'URGANCH'
    XAZORASP = '4X7', 'XAZORASP'
    XIVA = '4X8', 'XIVA'
    XONQA = '4X9', 'XONQA'
    YANGIARIQ = '4X10', 'YANGIARIQ'
    YANGIBOZOR = '4X11', 'YANGIBOZOR'

    # BUXORO
    BUXORO_SHAHRI = '5X1', 'BUXORO_SHAHRI'
    BUXORO = '5X2', 'BUXORO'
    GIJDUVON = '5X3', 'GIJDUVON'
    JONDOR = '5X4', 'JONDOR'
    KOGON_SHAHRI = '5X5', 'KOGON_SHAHRI'
    KOGON = '5X6', 'KOGON'
    OLOT = '5X7', 'OLOT'
    PESHKU = '5X8', 'PESHKU'
    QORAKOL = '5X9', 'QORAKOL'
    QOROVULBOZOR = '5X10', 'QOROVULBOZOR'
    ROMITAN = '5X11', 'ROMITAN'
    SHOFIRKON = '5X12', 'SHOFIRKON'
    VOBKENT = '5X13', 'VOBKENT'

    # SURXONDARYO
    ANGOR = '6X1', 'ANGOR'
    BANDIXON = '6X2', 'BANDIXON'
    BOYSUN = '6X3', 'BOYSUN'
    DENOV = '6X4', 'DENOV'
    JARQORGON = '6X5', 'JARQORGON'
    MUZROBOT = '6X6', 'MUZROBOT'
    OLTINSOY = '6X7', 'OLTINSOY'
    QIZIRIQ = '6X8', 'QIZIRIQ'
    QUMQORGON = '6X9', 'QUMQORGON'
    SARIOSIYO = '6X10', 'SARIOSIYO'
    SHEROBOD = '6X11', 'SHEROBOD'
    SHORCHI = '6X12', 'SHORCHI'
    TERMIZ_SHAHRI = '6X13', 'TERMIZ_SHAHRI'
    TERMIZ = '6X14', 'TERMIZ'
    UZUN = '6X15', 'UZUN'

    # NAMANGAN
    CHORTOQ = '7X1', 'CHORTOQ'
    CHUST = '7X2', 'CHUST'
    KOSONSOY = '7X3', 'KOSONSOY'
    MINGBULOQ = '7X4', 'MINGBULOQ'
    NAMANGAN_SHAHRI = '7X5', 'NAMANGAN_SHAHRI'
    NAMANGAN = '7X6', 'NAMANGAN'
    NORIN = '7X7', 'NORIN'
    POP = '7X8', 'POP'
    TORAQORGON = '7X9', 'TORAQORGON'
    UCHQORGON = '7X10', 'UCHQORGON'
    UYCHI = '7X11', 'UYCHI'
    YANGIQORGON = '7X12', 'YANGIQORGON'

    # ANDIJON
    ANDIJON_SHAHRI = '8X1', 'ANDIJON_SHAHRI'
    ANDIJON = '8X2', 'ANDIJON'
    ASAKA = '8X3', 'ASAKA'
    BALIQCHI = '8X4', 'BALIQCHI'
    BOZ = '8X5', 'BOZ'
    BULOQBOSHI = '8X6', 'BULOQBOSHI'
    IZBOSKAN = '8X7', 'IZBOSKAN'
    JALOLQUDUQ = '8X8', 'JALOLQUDUQ'
    MARHAMAT = '8X9', 'MARHAMAT'
    OLTINKOL = '8X10', 'OLTINKOL'
    PAXTAOBOD = '8X11', 'PAXTAOBOD'
    QORGONTEPA = '8X12', 'QORGONTEPA'
    SHAHRIXON = '8X13', 'SHAHRIXON'
    ULUGNOR = '8X14', 'ULUGNOR'
    XOJAOBOD = '8X15', 'XOJAOBOD'
    XONOBOD_SHAHRI = '8X16', 'XONOBOD_SHAHRI'

    # QASHQADARYO
    CHIROQCHI = '9X1', 'CHIROQCHI'
    DEHQONOBOD = '9X2', 'DEHQONOBOD'
    GUZOR = '9X3', 'GUZOR'
    KASBI = '9X4', 'KASBI'
    KITOB = '9X5', 'KITOB'
    KOSON = '9X6', 'KOSON'
    MIRISHKOR = '9X7', 'MIRISHKOR'
    MUBORAK = '9X8', 'MUBORAK'
    NISHON = '9X9', 'NISHON'
    QAMASHI = '9X10', 'QAMASHI'
    QARSHI_SHAHRI = '9X11', 'QARSHI_SHAHRI'
    QARSHI = '9X12', 'QARSHI'
    SHAHRISABZ_SHAHRI = '9X13', 'SHAHRISABZ_SHAHRI'
    YAKKABOG = '9X14', 'YAKKABOG'

    # SAMARQAND
    BULUNGUR = '10X1', 'BULUNGUR'
    ISHTIXON = '10X2', 'ISHTIXON'
    JOMBOY = '10X3', 'JOMBOY'
    KATTAQORGON_SHAXRI = '10X4', 'KATTAQORGON_SHAXRI'
    KATTAQORGON = '10X5', 'KATTAQORGON'
    NARPAY = '10X6', 'NARPAY'
    NUROBOD = '10X7', 'NUROBOD'
    OQDARYO = '10X8', 'OQDARYO'
    PAST_DARGOM = '10X9', 'PAST_DARGOM'
    PAXTACHI = '10X10', 'PAXTACHI'
    POYARIQ = '10X11', 'POYARIQ'
    QOSHRABOT = '10X12', 'QOSHRABOT'
    SAMARQAND_SHAXRI = '10X13', 'SAMARQAND'
    SAMARQAND = '10X14', 'SAMARQAND'
    TOYLOQ = '10X15', 'TOYLOQ'
    URGUT = '10X16', 'URGUT'

    # FARGONA
    BESHARIQ = '11X1', 'BESHARIQ'
    BOGDOD = '11X2', 'BOGDOD'
    BUVAYDA = '11X3', 'BUVAYDA'
    DANGARA = '11X4', 'DANGARA'
    FARGONA_SHAHRI = '11X5', 'FARGONA_SHAHRI'
    FARGONA = '11X6', 'FARGONA'
    FURQAT = '11X7', 'FURQAT'
    MARGILON_SHAHRI = '11X8', 'MARGILON_SHAHRI'
    OZBEKISTON = '11X9', 'OZBEKISTON'
    OLTIARIQ = '11X10', 'OLTIARIQ'
    QOQON_SHAHRI = '11X11', 'QOQON_SHAHRI'
    QOSHTEPA = '11X12', 'QOSHTEPA'
    QUVA = '11X13', 'QUVA'
    QUVASOY_SHAHRI = '11X14', 'QUVASOY_SHAHRI'
    RISHTON = '11X15', 'RISHTON'
    SOX = '11X16', 'SOX'
    TOSHLOQ = '11X17', 'TOSHLOQ'
    UCHKOPRIK = '11X18', 'UCHKOPRIK'
    YOZYOVON = '11X19', 'YOZYOVON'

    # TOSHKENT
    BEKTEMIR = '12X1', 'BEKTEMIR'
    MIROBOD = '12X2', 'MIROBOD'
    MIRZO_ULUGBEK = '12X3', 'MIRZO_ULUG‘BEK'
    SERGELI = '12X4', 'SERGELI'
    OLMAZOR = '12X5', 'OLMAZOR'
    UCHTEPA = '12X6', 'UCHTEPA'
    SHAYXONTOHUR = '12X7', 'SHAYXONTOHUR'
    YASHNOBOD = '12X8', 'YASHNOBOD'
    CHILONZOR = '12X9', 'CHILONZOR'
    YUNUSOBOD = '12X10', 'YUNUSOBOD'
    YAKKASAROY = '12X11', 'YAKKASAROY'

    # QORAQALPOGISTON
    AMUDARYO = '13X1', 'AMUDARYO'
    BERUNIY = '13X2', 'BERUNIY'
    CHIMBOY = '13X3', 'CHIMBOY'
    ELLIKQALA = '13X4', 'ELLIKQALA'
    KEGEYLI = '13X5', 'KEGEYLI'
    MOYNOQ = '13X6', 'MOYNOQ'
    NUKUS_SHAHRI = '13X7', 'NUKUS_SHAHRI'
    NUKUS = '13X8', 'NUKUS'
    QONLIKOL = '13X9', 'QONLIKOL'
    QORAUZAQ = '13X10', 'QORAUZAQ'
    QUNGIROT = '13X11', 'QUNGIROT'
    SHUMANAY = '13X12', 'SHUMANAY'
    TAXIATOSH_SHAHRI = '13X13', 'TAXIATOSH_SHAHRI'
    TAXTAKOPIR = '13X14', 'TAXTAKOPIR'
    TORTKOL = '13X15', 'TORTKOL'
    XOJAYLI = '13X16', 'XOJAYLI'