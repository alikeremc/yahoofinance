def fiyat_temizle(formatli_fiyat):
        # noktalama işaretli, sonunda TL olan fiyatı temizleme
    bosluk_yeri = formatli_fiyat.find(' ')

    raw_fiyat = formatli_fiyat[:bosluk_yeri]

    nokta_yeri = raw_fiyat.find(".")

    if nokta_yeri >= 0:
        fiyat = raw_fiyat[0:nokta_yeri] + raw_fiyat[nokta_yeri + 1:]

    fiyat = int(fiyat)
    return fiyat
