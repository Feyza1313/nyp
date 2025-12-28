import random

class AcilDurumBirim:
    def __init__(self, isim, saglik_sorunu=False):
        self.isim = isim
        self.saglik_sorunu = saglik_sorunu
        self.gorev_suresi = 0
        self.fazla_mesai_ucreti = 0
        self.aktif = True

    def calisma_istegi_sor(self):
        if not self.aktif:
            return False
        cevap = input(f"{self.isim} çalışmak istiyor mu? (e/h): ").lower()
        if cevap != 'e':
            if not self.saglik_sorunu:
                self.aktif = False
                print(f"{self.isim} işten çıkarıldı (çalışmak istemedi).")
            return False
        return True

    def gorev_yap(self, saat):
        raise NotImplementedError

class SaglikEkibi(AcilDurumBirim):
    def gorev_yap(self, saat):
        if not self.aktif:
            return 0
        if self.calisma_istegi_sor():
            self.gorev_suresi += saat
            mesai = max(0, saat-8)*90
            self.fazla_mesai_ucreti += mesai
            print(f"{self.isim} sağlık ekibi görev yaptı, fazla mesai: {mesai} TL")
            return mesai
        return 0

class GuvenlikEkibi(AcilDurumBirim):
    def gorev_yap(self, saat):
        if not self.aktif:
            return 0
        if self.calisma_istegi_sor():
            self.gorev_suresi += saat
            mesai = max(0, saat-8)*90
            self.fazla_mesai_ucreti += mesai
            print(f"{self.isim} güvenlik ekibi görev yaptı, fazla mesai: {mesai} TL")
            return mesai
        return 0

def gunluk_istatistik(ekipler):
    toplam_fazla_mesai = sum(e.fazla_mesai_ucreti for e in ekipler if e.aktif)
    aktif_ekip = sum(1 for e in ekipler if e.aktif)
    isten_cikan = sum(1 for e in ekipler if not e.aktif)
    print("\n--- Günlük Fazla Mesai ve İş Durumu ---")
    for e in ekipler:
        durum = "Çalışıyor" if e.aktif else "İşten çıkarıldı"
        print(f"{e.isim}: {durum}")
    print(f"Aktif çalışan sayısı: {aktif_ekip}")
    print(f"İşten çıkarılan sayısı: {isten_cikan}")
    print(f"Toplam fazla mesai ödemesi: {toplam_fazla_mesai} TL\n")

# Örnek Kullanım
ekipler = [
    SaglikEkibi("Dr. Ahmet"),
    SaglikEkibi("Hemşire Ayşe"),
    GuvenlikEkibi("Polis Cenk"),
    GuvenlikEkibi("Asker Elif", saglik_sorunu=True)
]

# 1 günlük görev simülasyonu
for e in ekipler:
    e.gorev_yap(random.randint(8,12))

gunluk_istatistik(ekipler)
