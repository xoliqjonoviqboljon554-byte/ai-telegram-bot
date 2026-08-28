import os
import time
import telebot
import google.generativeai as genai

# Railway'dagi Variables'dan token va kalitni o'qiydi
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
KANAL_USERNAME = "@ai_uz_lab"

# Gemini va Telegram botni sozlash
genai.configure(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

print("Bot ishga tushdi va har 10 sekundda post yuborishni boshladi...")

# Bot tinimsiz 24/7 ishlashi uchun sikl
while True:
    try:
        # Gemini orqali qisqa post matnini generatsiya qilish
        model = genai.GenerativeModel("gemini-pro")
        prompt = "Telegram kanali uchun qiziqarli, qisqa va foydali bitta gapli fakt yoki motivatsiya yozib ber (o'zbek tilida)."
        response = model.generate_content(prompt)
        
        post_matni = response.text
        
        # Kanalga yuborish
        bot.send_message(KANAL_USERNAME, post_matni)
        print("Post muvaffaqiyatli yuborildi!")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    
    # 10 sekund kutish
    time.sleep(10)