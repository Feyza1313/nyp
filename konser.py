print("\n==================== KONSERLER İPTAL EDİLDİ ====================")
import random
# Konum bazlı risk kontrolü
class KonumRisk:
    def __init__(self, isim, konum):
        self.isim = isim
        self.__konum = konum  # kapsülleme
        self.risk_skor = 0

    def risk_hesapla(self, kalabalik_bolge):
        if kalabalik_bolge:
            self.risk_skor = 5  # yüksek risk
        else:
            self.risk_skor = 2  # düşük risk

    def risk_uyarisi(self):
        if self.risk_skor >= 5:
            print(f"{self.isim} ⚠ Yüksek riskli bölgede! Konser iptal.")
        else:
            print(f"{self.isim} düşük riskli bölgede, dikkat et.")

    def konum_goster(self):  # kapsülleme örneği
        return self.__konum

# STATIC ve CLASS method örneği
class KonserSistemi:
    toplam_kisi = 0  # class attribute

    @classmethod
    def kisi_ekle(cls, sayi):
        cls.toplam_kisi += sayi

    @staticmethod
    def konser_uyarisi():
        print("⚠ Konserler iptal edildi, kalabalıktan uzak durun!")

# Kullanım
KonserSistemi.konser_uyarisi()

kisiler = [
    KonumRisk("Ali", (5,5)),
    KonumRisk("Ayşe", (10,12))
]

for kisi in kisiler:
    # Rastgele kalabalık belirle
    kalabalik = random.choice([True, False])
    kisi.risk_hesapla(kalabalik)
    kisi.risk_uyarisi()
    KonserSistemi.kisi_ekle(1)

print(f"Toplam riskli kişi sayısı: {KonserSistemi.toplam_kisi}")
