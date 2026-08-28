import time
import telebot
import feedparser
import os
import random
import re

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("Maqola rasmi bilan ishlaydigan Global AI boti ishga tushdi...")

RSS_URLS = [
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"
]

zaxira_rasmlar = [
    "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1000",
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000",
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1000",
    "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=1000"
]

def get_sent_links():
    if os.path.exists("sent_links.txt"):
        with open("sent_links.txt", "r") as f:
            return set(line.strip() for line in f)
    return set()

def save_link(link):
    with open("sent_links.txt", "a") as f:
        f.write(link + "\n")

# Maqolaning o'zidan rasmni qidirib topish funksiyasi
def extract_image(entry):
    # 1. Media content orqali qidirish
    if hasattr(entry, 'media_content') and entry.media_content:
        for media in entry.media_content:
            if 'url' in media:
                return media['url']
    
    # 2. Enclosures orqali qidirish
    if hasattr(entry, 'enclosures') and entry.enclosures:
        for enc in entry.enclosures:
            if 'image' in enc.get('type', ''):
                return enc.href
                
    # 3. Summary yoki content ichidan <img> tegini qidirish
    content_html = ""
    if hasattr(entry, 'summary'):
        content_html += entry.summary
    if hasattr(entry, 'content'):
        for c in entry.content:
            content_html += c.value
            
    img_match = re.search(r'<img[^>]+src="([^">]+)"', content_html)
    if img_match:
        return img_match.group(1)
        
    # Agar topilmasa zaxiradagidan tasodifiy tanlaymiz
    return random.choice(zaxira_rasmlar)

yuborilgan_yangiliklar = get_sent_links()

while True:
    try:
        for rss_url in RSS_URLS:
            feed = feedparser.parse(rss_url)
            
            for entry in reversed(feed.entries):
                link = entry.link
                
                if link not in yuborilgan_yangiliklar:
                    sarlavha = entry.title
                    
                    caption = f"🤖 **Global AI Yangiligi**\n\n📌 **{sarlavha}**\n\n🔗 Batafsil o'qish (Manba): {link}\n\n@ai_uz_lab"
                    
                    # Maqolaga mos rasmni olamiz
                    maqola_rasmi = extract_image(entry)
                    unikal_foto = f"{maqola_rasmi}&t={time.time()}"
                    
                    bot.send_photo(
                        chat_id=KANAL_USERNAME,
                        photo=unikal_foto,
                        caption=caption,
                        parse_mode="Markdown"
                    )
                    
                    yuborilgan_yangiliklar.add(link)
                    save_link(link)
                    print(f"Yuborildi (asl rasmi bilan): {sarlavha}")
                    break
            
            time.sleep(2)
                
    except Exception as e:
        print(f"Xato: {e}")
    
    time.sleep(30)