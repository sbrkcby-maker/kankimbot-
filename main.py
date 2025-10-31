

TELEGRAM_BOT_TOKEN = "8327583891:AAFO8pYnscCFTjiFZYzq8IT4vDyHPxv8X4I"
CHAT_ID = "BURAYA_CHAT_ID_YAZ"  # Telegram'da botla konuşup /start deyince getUpdates’ten alacağın ID

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram hatası:", e)

while True:
    try:
        # Basit örnek sinyal: rastgele fiyat kontrolü gibi düşünebilirsin
        send_message("✅ Bot aktif! Coinleri tarıyor...")
        time.sleep(60)
    except Exception as e:
        send_message(f"⚠️ Hata oluştu: {e}")
        time.sleep(30)
