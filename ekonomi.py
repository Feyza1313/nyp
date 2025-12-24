import random

class EkonomiDestek:
    def __init__(self):
        self.raporlar = []

    def vatandas_al(self):
        print("\n--- Vatandaş Bilgileri ---")
        isim = input("İsim: ")
        gelir = int(input("Aylık gelir (TL): "))
        kira = int(input("Aylık kira (TL): "))
        fatura = int(input("Aylık fatura (TL): "))

        return {
            "isim": isim,
            "gelir": gelir,
            "kira": kira,
            "fatura": fatura
        }

    def destek_degerlendir(self, v):
        print("\n==============================")
        print(f"{v['isim']} için değerlendirme yapılıyor")

        # Gelir ve giderler
        gelir = v["gelir"]
        kira = v["kira"]
        fatura = v["fatura"]

        # Toplam gider
        toplam_gider = kira + fatura

        # İlk bakiye
        ilk_bakiye = gelir - toplam_gider

        print("\n--- GELİR / GİDER ---")
        print(f"Gelir : {gelir} TL")
        print(f"Kira  : {kira} TL")
        print(f"Fatura: {fatura} TL")
        print(f"Toplam gider: {toplam_gider} TL")
        print(f"İlk bakiye  : {ilk_bakiye} TL")

        # Devlet desteği kontrolü
        if ilk_bakiye < 0:
            print("\n⚠️ Gelir giderleri karşılamıyor")
            print("Devlet en az maliyetli desteği uyguluyor")
            print("➡️ Fatura devlet tarafından ödendi")

            # Sadece faturayı düş
            toplam_gider = toplam_gider - fatura

        else:
            print("\n✔️ Gelir yeterli, destek gerekmedi")

        # Son bakiye
        son_bakiye = gelir - toplam_gider

        print("\n--- AY SONU ---")
        print(f"Güncel gider: {toplam_gider} TL")
        print(f"Son bakiye : {son_bakiye} TL")

        # Rapor kaydı
        self.raporlar.append({
            "isim": v["isim"],
            "gelir": gelir,
            "gider": toplam_gider,
            "kalan": son_bakiye
        })

    def rapor(self):
        print("\n===== GENEL RAPOR =====")
        for r in self.raporlar:
            print("----------------------")
            print(f"İsim : {r['isim']}")
            print(f"Gelir: {r['gelir']} TL")
            print(f"Gider: {r['gider']} TL")
            print(f"Kalan: {r['kalan']} TL")
        print("----------------------")


# --------- PROGRAMI ÇALIŞTIR ---------
if __name__ == "__main__":
    sistem = EkonomiDestek()
    vatandas = sistem.vatandas_al()
    sistem.destek_degerlendir(vatandas)
    sistem.rapor()
