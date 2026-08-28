import time
import telebot

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("Ultra Pro Max Bot ishga tushdi va kanalga xizmat ko'rsatmoqda...")

# Ultra Pro Max darajasidagi boy va xilma-xil postlar bazasi
postlar = [
    {
        "photo": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1000&auto=format&fit=crop",
        "caption": "💻 **Ultra Dars 1:** Python dasturlash tilida o'zgaruvchilar va ma'lumotlar turlari.\n\nNoldan boshlayotganlar uchun eng tushunarli va mukammal qo'llanma! 🚀\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1677442136019-21780efad99a?q=80&w=1000&auto=format&fit=crop",
        "caption": "🤖 **AI Yangilik:** Sun'iy intellekt olamidagi eng so'nggi va hayratlanarli yangiliklar.\n\nHar kuni texnologiya olamida nima o'zgarmoqda? Biz bilan kuzatib boring! 💡\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1000&auto=format&fit=crop",
        "caption": "⚡️ **Amaliy Dars:** Telegram bot yaratish sirlari va `telebot` kutubxonasi.\n\nO'z botingizni bugunoq qanday ishga tushirish mumkin? To'liq qo'llanma! 🔥\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=1000&auto=format&fit=crop",
        "caption": "🎯 **Pro Prompt:** ChatGPT va Claude uchun eng sara va kuchli buyruqlar.\n\nSun'iy intellektdan 10x samaraliroq foydalanish sirini o'rganing! 🧠\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?q=80&w=1000&auto=format&fit=crop",
        "caption": "🌐 **Web Dars:** HTML va CSS yordamida zamonaviy veb-sahifa yaratish.\n\nFrontend olamiga ilk qadamni tashlang va o'z dizayningizni yarating! 🎨\n\n@ai_uz_lab"
    }
]

index = 0

while True:
    try:
        # Har safar keyingi postga o'tadi va takrorlanmaydi
        current_post = postlar[index % len(postlar)]
        
        bot.send_photo(
            chat_id=KANAL_USERNAME, 
            photo=current_post["photo"], 
            caption=current_post["caption"], 
            parse_mode="Markdown"
        )
        print(f"Ultra Post {index + 1} muvaffaqiyatli yuborildi!")
        
        index += 1
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    
    # Har 30 sekundda navbatdagi mukammal postni yuboradi
    time.sleep(30)