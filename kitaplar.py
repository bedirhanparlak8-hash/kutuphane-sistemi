kitaplar = []

def kitap_ekle(yeni_kitap):
    kitaplar.append(yeni_kitap)
    print(f"✅ Başarıyla eklendi: {yeni_kitap}")
    
def kitap_sil(kitap_adi):
    if kitap_adi in kitaplar:
        kitaplar.remove(kitap_adi)
        print(f"❌ Silindi: {kitap_adi}")
    else:
        print(f"⚠️ Hata: '{kitap_adi}' listede bulunamadı!")


def kitap_listele():
    print("\n📚 KÜTÜPHANE LİSTESİ 📚")
    if not kitaplar:
        print("Şu an kütüphane boş.")
    else:
        for kitap in kitaplar:
            print(f"- {kitap}")

# Test edelim
if __name__ == "__main__":
    kitap_ekle("Nutuk")
    kitap_sil("Nutuk")
    kitap_listele()
    kitap_ekle("Küçük Prens")
    kitap_listele()
def kitap_sil(kitap_adi):
    if kitap_adi in kitaplar:
        kitaplar.remove(kitap_adi)
        print(f"❌ Silindi: {kitap_adi}")
    else:
        print(f"⚠️ Hata: '{kitap_adi}' listemizde yok!")

# Dosyanın en altındaki test kısmını şöyle güncelle:
if __name__ == "__main__":
    kitap_ekle("Nutuk")
    kitap_ekle("Küçük Prens")
    kitap_listele()
    
    kitap_sil("Nutuk") # Silme özelliğini test ediyoruz
    kitap_listele()