kitaplar = []

def kitap_ekle(yeni_kitap):
    kitaplar.append(yeni_kitap)
    print(f"✅ Başarıyla eklendi: {yeni_kitap}")

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
    kitap_ekle("Küçük Prens")
    kitap_listele()