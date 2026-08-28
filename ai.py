import time
import telebot
import random

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("Bot muvaffaqiyatli ishga tushdi...")

postlar = [
    {
        "photo": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000",
        "caption": "💻 **Dars 1: Python'da O'zgaruvchilar**\n\nAssalomu alaykum! Bugundan Python o'rganishni boshlaymiz. O'zgaruvchi — bu ma'lumot saqlash uchun quti. 🚀\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1000",
        "caption": "🤖 **IT Yangilik: Sun'iy Intellekt**\n\nSun'iy intellekt texnologiyalari har kuni rivojlanib, dasturlashni tezlashtirmoqda. 💡\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1000",
        "caption": "⚡️ **Amaliyot: Telegram Bot**\n\nO'z botingizni yaratish uchun `telebot` kutubxonasidan foydalanamiz. 🔥\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=1000",
        "caption": "🎯 **Maslahat: To'g'ri Prompt Yozish**\n\nChatGPT va boshqa neyrotarmoqlardan to'g'ri foydalanish uchun aniq vazifa qo'ying! 🧠\n\n@ai_uz_lab"
    }
]

last_index = -1

while True:
    try:
        # Takrorlanmaydigan tasodifiy indeks tanlaymiz
        index = random.randint(0, len(postlar) - 1)
        while index == last_index:
            index = random.randint(0, len(postlar) - 1)
        last_index = index
        
        current_post = postlar[index]
        
        # Telegram keshini aldash uchun vaqt qo'shamiz
        unikal_foto = f"{current_post['photo']}&t={time.time()}"
        
        bot.send_photo(
            chat_id=KANAL_USERNAME, 
            photo=unikal_foto, 
            caption=current_post["caption"], 
            parse_mode="Markdown"
        )
        print(f"Post {index + 1} muvaffaqiyatli yuborildi!")
        
    except Exception as e:
        print(f"Xato: {e}")
    
    # Har 10 soniya kutish
    time.sleep(10)
