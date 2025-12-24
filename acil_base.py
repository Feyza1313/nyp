from abc import ABC, abstractmethod

print("------------------112 ACİL DURUM SİSTEMİ-------------------")

# Ambulansa gelen çağrı sayısı
cagri_sayisi = int(input("Ambulansa kaç çağrı geldi?: "))

# ---------------- ABSTRACT BASE CLASS ----------------
class AcilDurumBirim(ABC): #abstract+override 
    def __init__(self, birim_id):
        self.birim_id = birim_id

    @abstractmethod
    def uyarı_al(self, mesaj):
        pass
