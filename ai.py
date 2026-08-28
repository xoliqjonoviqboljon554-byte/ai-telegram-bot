import time
import telebot

# Telegram bot tokeningizni yozing
TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("Bot ishga tushdi va xatolarsiz ishlamoqda...")

# Kanalga yuboriladigan tayyor darslar va yangiliklar ro'yxati
postlar = [
    "📚 **Dars 1:** Python dasturlash tilida o'zgaruvchilar (Variables) bilan ishlash. O'zgaruvchi — bu ma'lumotlarni saqlash uchun quti.",
    "🚀 **IT Yangilik:** Sun'iy intellekt sohasida bugun yangi tekin modellar taqdim etildi va ularning tezligi ancha oshdi.",
    "📚 **Dars 2:** Telegram bot yaratishda `telebot` kutubxonasidan foydalanish va xabarlarga javob berish mantiqi.",
    "🚀 **IT Yangilik:** Dasturchilar uchun sun'iy intellekt yordamchulari endi kod yozishni yanada tezlashtirmoqda."
]

index = 0

while True:
    try:
        # Navbatdagi postni tanlaymiz
        post_matni = postlar[index % len(postlar)]
        
        # Kanalga yuborish
        bot.send_message(KANAL_USERNAME, post_matni, parse_mode="Markdown")
        print("Post muvaffaqiyatli yuborildi!")
        
        index += 1
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    
    # Har 30 sekundda bitta post yuboradi (vaqtini o'zgartirishingiz mumkin)
    time.sleep(30)