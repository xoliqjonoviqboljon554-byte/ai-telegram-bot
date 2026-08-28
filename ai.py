import time
import telebot
import feedparser  # Internetdagi yangiliklarni o'qish uchun kutubxona

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("Google yangiliklarini avtomatik ulash boti ishga tushdi...")

# Google News RSS orqali IT va Sun'iy intellekt bo'yicha eng so'nggi yangiliklar olinadigan havola
RSS_URL = "https://news.google.com/rss/search?q=artificial+intelligence+programming&hl=uz&gl=UZ&ceid=UZ:uz"

yuborilgan_yangiliklar = set()

while True:
    try:
        print("Google'dan yangi ma'lumotlar tekshirilmoqda...")
        feed = feedparser.parse(RSS_URL)
        
        # Yangiliklarni tekshirib chiqamiz
        for entry in feed.entries[:5]:
            link = entry.link
            
            # Agar bu yangilik oldin yuborilmagan bo'lsa
            if link not in yuborilgan_yangiliklar:
                sarlavha = entry.title
                
                # Kanalga tashlanadigan xabar matni
                caption = f"🔥 **Google'dan Yangi Xabar / Dars**\n\n📌 **{sarlavha}p**\n\n🔗 Batafsil o'qish uchun havolaga o'ting: {link}\n\n@ai_uz_lab"
                
                # Tasodifiy IT mavzusidagi rasm
                foto = "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000"
                
                bot.send_photo(
                    chat_id=KANAL_USERNAME,
                    photo=foto,
                    caption=caption,
                    parse_mode="Markdown"
                )
                
                # Yuborilganini eslab qolamiz
                yuborilgan_yangiliklar.add(link)
                print(f"Yangi post yuborildi: {sarlavha}")
                
                # Har bir xabar orasida ozgina kutish
                time.sleep(5)
                break
                
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
    
    # Har 10 sekundda (yoki o'zingiz xohlagan vaqtda) Google'ni qayta tekshiradi
    time.sleep(10)