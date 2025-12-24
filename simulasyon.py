import random

# ------------------ VATANDAŞ ------------------
class Vatandas:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        self.durum = "saglikli"  # saglikli, hasta, iyilesmis, olum
        self.asi_oldu = False
        self.asi_basarili = False
        self.bagisiklik_orani = 0.0
        self.defnedildi = False

    def asi_uygula(self, asi_turleri):
        if not self.asi_oldu:
            self.asi_oldu = True
            self.asi_basarili = random.random() < random.choice(list(asi_turleri.values()))
            self.bagisiklik_orani = random.uniform(0.2, 0.5)

    def durum_guncelle(self):
        if self.durum == "saglikli":
            hasta_olma = random.random() < 0.2
            if self.asi_basarili:
                hasta_olma *= (1 - self.bagisiklik_orani)
            if hasta_olma:
                self.durum = "hasta"
        elif self.durum == "hasta":
            olum = random.random() < 0.05
            if olum:
                self.durum = "olum"
            else:
                iyilesme = random.random() < 0.2
                if iyilesme:
                    self.durum = "iyilesmis"

    def bagisiklik_artir(self):
        if self.durum != "olum":
            artma = random.uniform(0.01, 0.1)
            self.bagisiklik_orani = min(self.bagisiklik_orani + artma, 0.95)

# ------------------ BÖLGE ------------------
class Bolge:
    def __init__(self, isim, kisi_sayisi):
        self.isim = isim
        self.vatandaslar = [Vatandas(f"{isim}_Vatandas{i+1}", random.randint(18,80)) for i in range(kisi_sayisi)]
        self.karantina = False

    def karantinayi_guncelle(self):
        hasta = sum(1 for v in self.vatandaslar if v.durum=="hasta")
        olum = sum(1 for v in self.vatandaslar if v.durum=="olum")
        self.karantina = (hasta + olum)/len(self.vatandaslar) > 0.1

# ------------------ MEZARLIK ------------------
class Mezarlik:
    def __init__(self, ad):
        self.ad = ad
        self.defnedilenler = []

    def defin_yap(self, vatandas):
        if vatandas.durum == "olum" and not vatandas.defnedildi:
            vatandas.defnedildi = True
            self.defnedilenler.append(vatandas.isim)

# ------------------ AŞI TÜRLERİ ------------------
asi_turleri = {"BioNTech":0.95,"Sinovac":0.75,"Moderna":0.93,"AstraZeneca":0.85}

# ------------------ ÖRNEK BÖLGELER ------------------
dunya = [
    Bolge("Muratpaşa/Antalya", 30),
    Bolge("Kepez/Antalya", 25),
    Bolge("Bornova/İzmir", 40),
]

mezarlik = Mezarlik("Merkez Mezarlığı")

# ------------------ SIMÜLASYON ------------------
for gun in range(1, 8):  # 7 gün
    print(f"\n=== Gün {gun} ===")
    for bolge in dunya:
        for v in bolge.vatandaslar:
            v.asi_uygula(asi_turleri)
            v.bagisiklik_artir()
            v.durum_guncelle()
            if v.durum=="olum":
                mezarlik.defin_yap(v)
        bolge.karantinayi_guncelle()

    # Günlük rapor
    for bolge in dunya:
        toplam = len(bolge.vatandaslar)
        saglikli = sum(1 for v in bolge.vatandaslar if v.durum=="saglikli")
        hasta = sum(1 for v in bolge.vatandaslar if v.durum=="hasta")
        iyilesmis = sum(1 for v in bolge.vatandaslar if v.durum=="iyilesmis")
        olum = sum(1 for v in bolge.vatandaslar if v.durum=="olum")
        asi_olan = sum(1 for v in bolge.vatandaslar if v.asi_oldu)

        # Toplamın doğru olduğundan emin olalım
        toplam_hesapla = saglikli + hasta + iyilesmis + olum
        assert toplam == toplam_hesapla, f"Toplam sayılar hatalı! {bolge.isim}"

        print(f"\nBölge: {bolge.isim}")
        print(f"Toplam kişi: {toplam}")
        print(f"Sağlıklı: {saglikli}")
        print(f"Hasta: {hasta}")
        print(f"İyileşen: {iyilesmis}")
        print(f"Ölü: {olum}")
        print(f"Aşılanan: {asi_olan}")
        print(f"Karantina: {'Evet' if bolge.karantina else 'Hayır'}")

print(f"\nDefnedilenler ({len(mezarlik.defnedilenler)} kişi): {', '.join(mezarlik.defnedilenler)}")
