Markdown

# 📂 Smart File Organizer (Akıllı Dosya Düzenleyici)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge) ![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Smart File Organizer**, bilgisayarınızdaki karmaşık klasörleri (örneğin İndirilenler/Downloads) saniyeler içinde tarayıp dosya türlerine göre (Resimler, Belgeler, Yazılım vb.) otomatik olarak kategorize eden ve temizleyen bir Python otomasyon aracıdır.

> **Amaç:** Manuel dosya düzenleme zahmetini ortadan kaldırmak ve düzenli bir çalışma ortamı sağlamak.

---

## 🚀 Özellikler

- **🔍 Otomatik Algılama:** Dosya uzantılarını (`.pdf`, `.jpg`, `.py` vb.) otomatik tanır.
- **🛡️ Güvenli Taşıma:** Dosyaları taşırken isim çakışması olursa (Duplicate) veri kaybını önlemek için uyarır ve raporlar.
- **📊 Detaylı Raporlama:** İşlem sonunda hangi kategoriden kaç dosya taşındığını gösteren bir özet sunar.
- **⚙️ Kolay Yapılandırma:** Yeni dosya türleri `FILE_CATEGORIES` sözlüğüne tek satırla eklenebilir.
- **⚡ Performans:** `os.scandir` kullanılarak büyük dizinlerde bile yüksek hızda çalışır.

---

## 🛠️ Kurulum

Projeyi yerel makinenize klonlayın:

```bash
git clone [https://github.com/hokaradag/Smart_File_Organizer.git](https://github.com/hokaradag/Smart_File_Organizer.git)
cd Smart_File_Organizer
```

Sanal ortamı (opsiyonel ama önerilen) kurun:


# Sanal ortamı oluşturun
```bash
python -m venv .venv
```

# Windows için aktifleştirme:
```bash
.venv\Scripts\activate
```

# Mac/Linux için aktifleştirme:
```bash
source .venv/bin/activate
```

💻 Kullanım
Terminali açın ve programı çalıştırın:
```bash
python main.py
```

Program sizden düzenlenecek klasörün tam yolunu isteyecektir:

Düzenlemek istediğiniz klasör yolunu yapıştırın: C:\Users\Adiniz\Downloads

📂 Proje Öncesi ve Sonrası
Önce:
```text
Downloads/
├── fatura.pdf
├── tatil.jpg
├── setup.exe
└── film.mp4
```

Sonra:
```text
Downloads/
├── Belgeler/
│   └── fatura.pdf
├── Resimler/
│   └── tatil.jpg
├── Yazilim/
│   └── setup.exe
└── Videolar/
    └── film.mp4
```
🏗️ Proje Yapısı
```text
Smart_File_Organizer/
├── main.py          # Ana uygulama kodu ve mantığı
├── README.md        # Proje dokümantasyonu
└── .gitignore       # Git tarafından yok sayılacak dosyalar
```
🔮 Yol Haritası (Roadmap)
Bu proje geliştirmeye açıktır. Gelecek sürümler için planlanan özellikler:

[ ] Grafik Arayüz (GUI) eklenmesi.

[ ] İşlem geri alma (Undo) özelliği.

[ ] Belirli tarih öncesi dosyaları arşivleme seçeneği.

🤝 İletişim
Geliştirici: Hamit O. Karadağ

GitHub: hokaradag