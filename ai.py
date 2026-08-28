import time
import telebot
import feedparser
import os

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("1 daqiqada bir tekshiradigan AI yangiliklari boti ishga tushdi...")

RSS_URL = "https://news.google.com/rss/search?q=sun'iy+intellekt+OR+neyrotarmoq+OR+artificial+intelligence&hl=uz&gl=UZ&ceid=UZ:uz"

def get_sent_links():
    if os.path.exists("sent_links.txt"):
        with open("sent_links.txt", "r") as f:
            return set(line.strip() for line in f)
    return set()

def save_link(link):
    with open("sent_links.txt", "a") as f:
        f.write(link + "\n")

yuborilgan_yangiliklar = get_sent_links()

while True:
    try:
        feed = feedparser.parse(RSS_URL)
        
        for entry in reversed(feed.entries):
            link = entry.link
            
            if link not in yuborilgan_yangiliklar:
                sarlavha = entry.title
                
                caption = f"🤖 **Sun'iy Intellekt Yangiligi**\n\n📌 **{sarlavha}**\n\n🔗 Batafsil o'qish: {link}\n\n@ai_uz_lab"
                foto = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1000"
                
                bot.send_photo(
                    chat_id=KANAL_USERNAME,
                    photo=foto,
                    caption=caption,
                    parse_mode="Markdown"
                )
                
                yuborilgan_yangiliklar.add(link)
                save_link(link)
                print(f"Yuborildi: {sarlavha}")
                break
                
    except Exception as e:
        print(f"Xato: {e}")
    
    # Har 1 daqiqada (60 soniyada) yangi xabarlarni tekshiradi
    time.sleep(60)