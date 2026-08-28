import time
import telebot
import random

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("Bot har xil rasmlar va matnlar bilan ishga tushdi...")

# Har xil mavzuga mos rasmlar va postlar ro'yxati
postlar = [
    {
        "photo": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1000&auto=format&fit=crop",
        "caption": "💻 **Dars 1:** Python dasturlash asoslari va o'zgaruvchilar bilan ishlash.\n\nDasturlashni noldan boshlayotganlar uchun maxsus qo'llanma! 🚀\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1677442136019-21780efad99a?q=80&w=1000&auto=format&fit=crop",
        "caption": "🤖 **IT Yangilik:** Sun'iy intellekt texnologiyalari yana bir bosqichga ko'tarildi.\n\nBugungi kunda har bir dasturchi AI vositalaridan foydalanishi muhim. 💡\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1000&auto=format&fit=crop",
        "caption": "📚 **Amaliy Dars:** Telegram bot yaratish sirlari.\n\n`telebot` kutubxonasi yordamida o'z botingizni qanday yoshda bo'lishidan qat'iy nazar tezda yarating! ⚡️\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=1000&auto=format&fit=crop",
        "caption": "🔥 **Foydali Maslahat:** ChatGPT va Claude uchun eng sara promptlar.\n\nTo'g'ri buyruq berish orqali sun'iy intellektdan 10 barobar ko'proq foyda oling! 🎯\n\n@ai_uz_lab"
    }
]

while True:
    try:
        # Tasodifiy (har safar har xil) postni tanlaymiz
        current_post = random.choice(postlar)
        
        bot.send_photo(
            chat_id=KANAL_USERNAME, 
            photo=current_post["photo"], 
            caption=current_post["caption"], 
            parse_mode="Markdown"
        )
        print("Har xil turdagi rasm va post muvaffaqiyatli yuborildi!")
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    
    # Har 30 sekundda bitta har xil rasm va post yuboradi
    time.sleep(30)