import random

class PandemiRisk:
    def __init__(self, isim):
        self.isim = isim
        self.maske = False
        self.mesafe = False
        self.kalabalik = False
        self.asi = False
        self.risk_skor = 0

    def bilgiler_al(self):
        self.maske = input(f"{self.isim}, maske taktın mı? (evet/hayır): ").lower() == "evet"
        self.mesafe = input(f"{self.isim}, sosyal mesafeye uyuyor musun? (evet/hayır): ").lower() == "evet"
        self.kalabalik = input(f"{self.isim}, kalabalığa girdin mi? (evet/hayır): ").lower() == "evet"
        self.asi = input(f"{self.isim}, aşı oldun mu? (evet/hayır): ").lower() == "evet"

    def risk_hesapla(self):
        self.risk_skor = 0
        self.risk_skor += 0 if self.maske else 2
        self.risk_skor += 0 if self.mesafe else 2
        self.risk_skor += 2 if self.kalabalik else 0
        self.risk_skor -= 1 if self.asi else 0
        self.risk_skor = max(self.risk_skor, 0)

    def risk_uyarisi(self):
        if self.risk_skor >= 5:
            durum = "YÜKSEK RİSK"
            mesaj = "⚠ Çok yüksek risk! Maske tak, mesafe uygula, kalabalığa girme!"
        elif self.risk_skor >= 3:
            durum = "ORTA RİSK"
            mesaj = "⚠ Orta risk var. Tedbirleri sıkı uygula."
        else:
            durum = "DÜŞÜK RİSK"
            mesaj = "✔ Düşük risk. Ama tedbiri bırakma."
        print(f"\n{self.isim} → Risk skoru: {self.risk_skor} → {durum}")
        print(mesaj)

# -------------------- KULLANIM --------------------
# Senin bilgilerini al
kullanici = PandemiRisk("Sen")
kullanici.bilgiler_al()
kullanici.risk_hesapla()
kullanici.risk_uyarisi()

# Rastgele 5 kişi ile karşılaştırma
print("\n--- Diğer kişiler ---")
for i in range(5):
    kisi = PandemiRisk(f"Kişi{i+1}")
    kisi.maske = random.choice([True, False])
    kisi.mesafe = random.choice([True, False])
    kisi.kalabalik = random.choice([True, False])
    kisi.asi = random.choice([True, False])
    kisi.risk_hesapla()
    print(f"{kisi.isim} → Tekrar pandemiye yakalanma riski(6 puan üzerinden) : {kisi.risk_skor}")
