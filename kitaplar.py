import json

kitaplar = []

def verileri_kaydet():
    with open("kutuphane.json", "w", encoding="utf-8") as f:
        json.dump(kitaplar, f, ensure_ascii=False, indent=4)

def verileri_yukle():
    global kitaplar
    try:
        with open("kutuphane.json", "r", encoding="utf-8") as f:
            kitaplar = json.load(f)
    except FileNotFoundError:
        kitaplar = []

def kitap_ekle(yeni_kitap):
    kitaplar.append(yeni_kitap)
    verileri_kaydet() # Her eklemede kaydet
    print(f"✅ Başarıyla eklendi: {yeni_kitap}")

def kitap_sil(kitap_adi):
    if kitap_adi in kitaplar:
        kitaplar.remove(kitap_adi)
        verileri_kaydet() # Her silmede kaydet
        print(f"❌ Silindi: {kitap_adi}")
    else:
        print(f"⚠️ Hata: '{kitap_adi}' listede yok!")

def kitap_listele():
    print("\n📚 KÜTÜPHANE LİSTESİ 📚")
    if not kitaplar:
        print("Şu an kütüphane boş.")
    else:
        for kitap in kitaplar:
            print(f"- {kitap}")

if __name__ == "__main__":
    verileri_yukle() # Program açılırken eski verileri çek
    kitap_ekle("Nutuk")
    kitap_ekle("Küçük Prens")
    kitap_listele()
    # kitap_sil("Nutuk") # Denemek istersen yorumu kaldır