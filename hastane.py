import random

class Hastane:
    def __init__(self, ad, konum):
        self.ad = ad
        self.konum = konum

        self.kapasite = 2000
        self.yogun_bakim_kapasite = 200

        self.doluluk_orani = 0
        self.yogun_bakim_doluluk = 0

        self.personel_sayisi = 50

        # Mesaj bayrakları (spam önler)
        self.genel_mesaj_gosterildi = False
        self.yb_mesaj_gosterildi = False

    def musait_mi(self):
        return True

    def hasta_ekle(self, yb=False):
        if yb:
            self.yogun_bakim_doluluk += 1

            if self.yogun_bakim_doluluk > self.yogun_bakim_kapasite:
                self.yogun_bakim_kapasite += 50
                self.personel_sayisi += 10   

                if not self.yb_mesaj_gosterildi:
                    print(
                        f"{self.ad} yoğun bakım genişletildi | "
                        f"Yeni YB kapasite: {self.yogun_bakim_kapasite} | "
                        f"Personel: {self.personel_sayisi}"
                    )
                    self.yb_mesaj_gosterildi = True

        else:
            self.doluluk_orani += 1

            if self.doluluk_orani > self.kapasite:
                self.kapasite += 500
                self.personel_sayisi += 20   

                if not self.genel_mesaj_gosterildi:
                    print(
                        f"{self.ad} genel kapasite artırıldı | "
                        f"Yeni kapasite: {self.kapasite} | "
                        f"Personel: {self.personel_sayisi}"
                    )
                    self.genel_mesaj_gosterildi = True

# Hastaneler
hastaneler = [
    Hastane("Merkez Hastanesi", (10,5)),
    Hastane("Sehir Hastanesi", (25,30)),
    Hastane("Universite Hastanesi", (5,20)),
    Hastane("Saglik Ocagi Hastanesi", (15,10))
]

# Simülasyon
for _ in range(10000):
    hastane = random.choice(hastaneler)
    yb = random.random() < 0.2
    hastane.hasta_ekle(yb)
