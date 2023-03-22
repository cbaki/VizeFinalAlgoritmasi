ogrenci_sayisi = int(input("Sınıftaki öğrenci sayısı: "))

ogrenci_notlari = {}
for i in range(ogrenci_sayisi):
    ogrenci_adi = input(f"{i+1}. öğrenci adı: ")
    vize_notu = int(input(f"{ogrenci_adi}'nin vize notu: "))
    final_notu = int(input(f"{ogrenci_adi}'nin final notu: "))
    ogrenci_notlari[ogrenci_adi] = {"vize": vize_notu, "final": final_notu}


harf_notlari = {}
for ogrenci, notlar in ogrenci_notlari.items():
    not_ortalamasi = (notlar["vize"] * 0.5) + (notlar["final"] * 0.5)
    if not_ortalamasi >= 90:
        harf_notu = "AA"
    elif not_ortalamasi >= 85:
        harf_notu = "BA"
    elif not_ortalamasi >= 80:
        harf_notu = "BB"
    elif not_ortalamasi >= 70:
        harf_notu = "CB"
    elif not_ortalamasi >= 60:
        harf_notu = "CC"
    elif not_ortalamasi >= 50:
        harf_notu = "DC"
    elif not_ortalamasi >= 45:
        harf_notu = "DD"
    else:
        harf_notu = "FF"
    harf_notlari[ogrenci] = harf_notu


siralama = sorted(harf_notlari.items(), key=lambda x: x[1])


print("Öğrenci notları (harf sırasına göre):")
for ogrenci, harf_notu in siralama:
    print("{}: {}".format(ogrenci, harf_notu))

