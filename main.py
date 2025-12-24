import os
import shutil
from pathlib import Path

# Hangi uzantı nereye gidiyor
FILE_CATEGORIES = {
    "Resimler": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Belgeler": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Yazilim": [".py", ".js", ".html", ".css", ".java", ".cpp", ".json"],
    "Arsivler": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videolar": [".mp4", ".avi", ".mkv", ".mov", ".flv"],
    "Sesler": [".mp3", ".wav", ".aac", ".flac"],
}


def get_category(extension: str) -> str:
    """
    Dosya uzantısına göre kategori ismini döndürür.
    Eğer listede yoksa 'Diger' kategorisini döndürür.
    """
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Diger"


def organize_directory(target_path: str) -> None:
    """
    Verilen yoldaki dosyaları kategorilere ayırıp klasörler.
    """

    # 1. Yol kontrolü
    if not os.path.exists(target_path):
        print(f"HATA: '{target_path}' yolu bulunamadı.")
        return

    print(f"--- Düzenleme Başlıyor: {target_path} ---\n")

    # İstatistik sayacı
    stats = {key: 0 for key in FILE_CATEGORIES.keys()}
    stats["Diger"] = 0

    # Klasörü tara
    # os.scandir() büyük klasörlerde os.listdir()'den daha hızlıdır.
    with os.scandir(target_path) as entries:
        for entry in entries:
            # Sadece dosya odak
            if entry.is_dir():
                continue

            # Dosya ismini ve uzantısını al
            file_path = Path(entry.path)
            file_extension = file_path.suffix.lower()  # .JPG -> .jpg yapar

            # Kategoriyi bul
            category = get_category(file_extension)

            # Hedef klasör yolu: Örn: C:/Downloads/Resimler
            destination_folder = os.path.join(target_path, category)

            # Klasör yoksa oluştur
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(f"[YENİ KLASÖR] {category} oluşturuldu.")

            # Dosyayı taşı
            destination_path = os.path.join(destination_folder, entry.name)

            try:
                # Eğer dosya zaten varsa taşıma hatası verir, bunu yönetelim:
                if os.path.exists(destination_path):
                    print(f"[ATLANIYOR] {entry.name} zaten {category} içinde var.")
                else:
                    shutil.move(entry.path, destination_path)
                    print(f"[TAŞINDI] {entry.name} -> {category}/")
                    stats[category] += 1
            except Exception as e:
                print(f"[HATA] {entry.name} taşınamadı. Sebep: {e}")

    # Özet Raporu
    print("\n--- İşlem Tamamlandı ---")
    print("Özet Rapor:")
    for cat, count in stats.items():
        if count > 0:
            print(f"- {cat}: {count} dosya")


if __name__ == "__main__":
    # Kullanıcıdan klasör yolu iste
    user_input = input("Düzenlemek istediğiniz klasör yolunu yapıştırın: ")

    # Tırnak işaretlerini temizle (Windows bazen yola tırnak ekler)
    clean_path = user_input.strip('"').strip("'")

    organize_directory(clean_path)
