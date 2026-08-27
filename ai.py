import os
import time
import google.generativeai as genai
import schedule
import telebot

# --- SOZLAMALAR (To'g'ridan-to'g'ri yozib qo'yilgan) ---
TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
GEMINI_API_KEY = "AQ.Ab8RN6IiY3LWsbfk9g0kIq0_13i84cc_MptOzh8mUeY4eYYkjg"
KANAL_USERNAME = "@ai_uz_lab"

# Ulanishlarni faollashtirish
genai.configure(api_key="AQ.Ab8RN6IiY3LWsbfk9g0kIq0_13i84cc_MptOzh8mUeY4eYYkjg")
model = genai.GenerativeModel("gemini-1.5-flash")
bot = telebot.TeleBot("8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM")


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
schedule.every(1).minutes.do(kanalga_post_yuborish)

print("Bot ishga tushdi va rejimni kutmoqda...")

# Ishga tushishi bilan bitta post yuborib tekshirish uchun:
kanalga_post_yuborish()

# Bot tinimsiz 24/7 ishlashi uchun sikl
while True:
  schedule.run_pending()
  time.sleep(1)