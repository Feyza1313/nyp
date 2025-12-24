from abc import ABC, abstractmethod

print("------------------112 ACİL DURUM SİSTEMİ-------------------")

# Ambulansa gelen çağrı sayısı
cagri_sayisi = int(input("Ambulansa kaç çağrı geldi?: "))

# ---------------- ABSTRACT CLASS ----------------
class AcilDurumBirim(ABC):
    def __init__(self, birim_id):
        self.birim_id = birim_id

    @abstractmethod
    def uyarı_al(self, mesaj):
        pass

# ---------------- EKİPLER ----------------
class AmbulansEkibi(AcilDurumBirim):
    def uyarı_al(self, mesaj):
        print(f"[{self.birim_id}] {mesaj}")


class HastaTespitEkibi(AcilDurumBirim):
    def uyarı_al(self, mesaj):
        print(f"[{self.birim_id}] {mesaj}")

    def hasta_tespit_et(self, kisi):
        print(f"\n{kisi['isim']} için değerlendirme yapılıyor...")

        if (
            kisi["ates"] >= 38
            and kisi["oksuruk"]
            and kisi["nefes"]
            and kisi["agri"]
        ):
            print(f"⚠ {kisi['isim']} ACİL HASTA!")
            return True
        else:
            print(f"{kisi['isim']} için acil durum yok.")
            return False


class HastaSevkEkibi(AcilDurumBirim):
    toplam_hasta = 0

    def uyarı_al(self, mesaj):
        print(f"[{self.birim_id}] {mesaj}")

    def hasta_al_ve_gotur(self, kisi):
        HastaSevkEkibi.toplam_hasta += 1
        print(f" {kisi['isim']} ambulansla hastaneye götürülüyor...")

    @classmethod
    def toplam_vaka_goster(cls):
        print("\n===== GÜN SONU RAPORU =====")
        print("Toplam ambulansla sevk edilen hasta:", cls.toplam_hasta)


# ---------------- NESNELER ----------------
tespit_ekibi = HastaTespitEkibi("Hasta Tespit Ekibi")
ambulans = AmbulansEkibi("Ambulans Ekibi")
sevk_ekibi = HastaSevkEkibi("Hasta Sevk Ekibi")


# ---------------- ÇAĞRILAR ----------------
for i in range(1, cagri_sayisi + 1):
    print(f"\n--- {i}. ACİL ÇAĞRI ---")

    isim = input("Hastanın adı: ")
    ates = float(input("Ateş değeri: "))

    oksuruk = input("Öksürük var mı? (evet/hayır): ").lower() == "evet"
    nefes = input("Nefeste daralma var mı? (evet/hayır): ").lower() == "evet"
    agri = input("Eklem / kemik ağrısı var mı? (evet/hayır): ").lower() == "evet"

    kisi = {
        "isim": isim,
        "ates": ates,
        "oksuruk": oksuruk,
        "nefes": nefes,
        "agri": agri
    }

    hasta_mi = tespit_ekibi.hasta_tespit_et(kisi)

    if hasta_mi:
        ambulans.uyarı_al("Acil vaka tespit edildi")
        sevk_ekibi.hasta_al_ve_gotur(kisi)
    else:
        print(f"{isim} evde izleme önerildi.")

# ---------------- RAPOR ----------------
HastaSevkEkibi.toplam_vaka_goster()
print("Vaka sayısı artıyor. Virüs bulaşıyor")
