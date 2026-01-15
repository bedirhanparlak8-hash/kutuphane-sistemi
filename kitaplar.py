kitaplar = []

def kitap_ekle(yeni_kitap):
    kitaplar.append(yeni_kitap)
    print(f"✅ Başarıyla eklendi: {yeni_kitap}")
    verileri_kaydet()
    
def kitap_sil(kitap_adi):
    if kitap_adi in kitaplar:
        kitaplar.remove(kitap_adi)
        print(f"❌ Silindi: {kitap_adi}")
    else:
        print(f"⚠️ Hata: '{kitap_adi}' listemizde yok!")
        verileri_kaydet()
import json

def verileri_kaydet():
    with open("kutuphane.json", "w", encoding="utf-8") as f:
        json.dump(kitaplar, f, ensure_ascii=False)

def verileri_yukle():
    global kitaplar
    try:
        with open("kutuphane.json", "r", encoding="utf-8") as f:
            kitaplar = json.load(f)
    except FileNotFoundError:
        kitaplar = []

def kitap_listele():
    print("\n📚 KÜTÜPHANE LİSTESİ 📚")
    if not kitaplar:
        print("Şu an kütüphane boş.")
    else:
        for kitap in kitaplar:
            print(f"- {kitap}")

if __name__ == "__main__":
    kitap_ekle("Nutuk")
    kitap_ekle("Küçük Prens")
    kitap_listele()
    
    kitap_sil("Nutuk")
    kitap_listele()