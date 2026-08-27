import os
import time
import google.generativeai as genai
import schedule
import telebot

# --- SOZLAMALAR ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
KANAL_USERNAME = "@ai_uz_lab"  # Kanalingiz username'i

# Ulanishlarni faollashtirish
genai.configure(api_key=GEMINI_API_KEY)
# Gemini modeli
model = genai.GenerativeModel("gemini-1.5-flash")
bot = telebot.TeleBot(TELEGRAM_TOKEN)


def kanalga_post_yuborish():
  try:
    # Gemini'dan sun'iy intellekt bo'yicha qiziqarli post yozishni so'raymiz
    prompt = (
        "Telegram kanal uchun sun'iy intellekt (AI) haqida yangilik, foydali"
        " prompt yoki qisqa amaliy dars tayyorla. Post qiziqarli,"
        " emojilar bilan bezatilgan va o'zbek tilida bo'lsin."
    )

    response = model.generate_content(prompt)
    post_matni = response.text

    # Kanalga xabar yuborish
    bot.send_message(KANAL_USERNAME, post_matni)
    print("Post muvaffaqiyatli kanalga yuborildi!")

  except Exception as e:
    print(f"Xatolik yuz berdi: {e}")


# --- AVTOMATIK VAQTni BELGILASH ---
# Sinov uchun har 1 soatda post tashlashi uchun:
schedule.every(1).hours.do(kanalga_post_yuborish)

print("Bot ishga tushdi va rejimni kutmoqda...")

# Ishga tushishi bilan bitta post yuborib tekshirish uchun:
kanalga_post_yuborish()

# Bot tinimsiz 24/7 ishlashi uchun sikl
while True:
  schedule.run_pending()
  time.sleep(1)