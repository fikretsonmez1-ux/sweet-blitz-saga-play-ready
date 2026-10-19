# Sweet Blitz Saga — Play-ready package

Bu repo, Sweet Blitz Saga oyununu Google Play'e hazırlamak için gereken web-proje dosyalarını içerir: PWA manifest, service worker, Capacitor konfigürasyonu ve yardımcı scriptler.

İçindekiler:
- index.html — oyun (tek dosyalık web uygulaması)
- manifest.json — PWA manifest
- service-worker.js — offline cache
- capacitor.config.json — Capacitor config
- package.json — npm/Capacitor scriptleri
- privacy-policy.html — Play Console için basit gizlilik sayfası
- scripts/generate_icons.py — ikon üretme scripti (Pillow gerektirir)
- icons/ — (üretilecek) icon-192.png ve icon-512.png

Hızlı başlama (yerel test):

1) Gereksinimler
- Node.js ve npm
- Python 3 + Pillow (ikon üretmek için)
- Android Studio (Android paketleme için)

2) İkonları oluştur

Önce Pillow yükleyin (isteğe bağlı):

```bash
python3 -m pip install --user pillow
```

Ardından ikon üretin:

```bash
python3 scripts/generate_icons.py
```

Bu işlem `icons/icon-192.png` ve `icons/icon-512.png` dosyalarını oluşturur.

3) Lokal sunucu ile test

```bash
npm install
npm run start
# sonra tarayıcıda http://localhost:5000 (serve default port) açın
```

4) Capacitor ile Android projesi oluşturma

```bash
# Capacitor kurulumunu yapın
npm install
npx cap init "Sweet Blitz Saga" "com.sweetblitz.saga"
# Android platformu ekle
npx cap add android
# Web içeriğini native'e kopyala
npx cap sync android
# Android Studio'da projeyi aç
npx cap open android
```

Android Studio'da:
- Target SDK sürümünü güncelleyin (Play gereksinimlerine göre).
- Build > Generate Signed Bundle / APK > Android App Bundle
- Keystore oluşturup imzalayın.
- AAB dosyasını Play Console'a yükleyin.

5) TWA alternatifi (PWA'yi Play'e koymak için)

Trusted Web Activity kullanmak isterseniz bubblewrap kullanabilirsiniz. Site HTTPS olmalı ve manifest/service worker düzgün çalışmalı.

6) Play Console için gerekli varlıklar
- App icon (512x512 PNG)
- Feature graphic (1024x500)
- Screenshots (en az 2, önerilen 4+) — telefon boyutları: 1080x1920
- Privacy policy URL (ör: host ettiğiniz privacy-policy.html)

7) Önemli notlar
- Uygulama veri toplamıyorsa bile Play Console'lardaki veri formunu doğru doldurun.
- Eğer reklam veya analitik ekleyecekseniz kullanıcı onaylarından (GDPR/CCPA) sorumlu olursunuz.

Herhangi bir adımda yardıma ihtiyacınız olursa yorum bırakın. Ben Android AAB üretim talimatlarını ve Play Console ekran görüntülerini adım adım hazırlayıp yüklemenize yardımcı olabilirim.
