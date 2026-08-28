import time
import telebot
import feedparser
import os
import random
import re
from deep_translator import GoogleTranslator

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("O'zbek tiliga tarjima qiluvchi va xilma-xil rasmli Global AI boti ishga tushdi...")

RSS_URLS = [
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"
]

# Turli xil va chiroyli mavzuli IT/AI rasmlari ro'yxati (har safar boshqasi tushishi uchun)
xilma_xil_rasmlar = [
    "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1000",
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000",
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1000",
    "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=1000",
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=1000",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1000",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1000",
    "https://images.unsplash.com/photo-1525373698358-043e1a415360?w=1000"
]

def get_sent_links():
    if os.path.exists("sent_links.txt"):
        with open("sent_links.txt", "r") as f:
            return set(line.strip() for line in f)
    return set()

def save_link(link):
    with open("sent_links.txt", "a") as f:
        f.write(link + "\n")

# Inglizcha matnni chiroyli o'zbek tiliga tarjima qilish
def translate_to_uzbek(text):
    try:
        translated = GoogleTranslator(source='en', target='uz').translate(text)
        return translated
    except:
        return text

# Maqoladan rasm topish yoki ro'yxatdan tasodifiy olish
def extract_image(entry, index):
    try:
        if hasattr(entry, 'media_content') and entry.media_content:
            for media in entry.media_content:
                if 'url' in media:
                    return media['url']
        
        content_html = ""
        if hasattr(entry, 'summary'):
            content_html += entry.summary
        if hasattr(entry, 'content'):
            for c in entry.content:
                content_html += c.value
                
        img_match = re.search(r'<img[^>]+src="([^">]+)"', content_html)
        if img_match:
            return img_match.group(1)
    except:
        pass
        
    # Agar maqolada rasm bo'lmasa, navbatdagi turli xil rasmdan foydalanamiz
    return xilma_xil_rasmlar[index % len(xilma_xil_rasmlar)]

yuborilgan_yangiliklar = get_sent_links()
counter = 0

while True:
    try:
        for rss_url in RSS_URLS:
            feed = feedparser.parse(rss_url)
            
            for entry in reversed(feed.entries):
                link = entry.link
                
                if link not in yuborilgan_yangiliklar:
                    # Sarlavhani o'zbek tiliga tarjima qilamiz
                    inglizcha_sarlavha = entry.title
                    uzbekcha_sarlavha = translate_to_uzbek(inglizcha_sarlavha)
                    
                    caption = f"🤖 **Global AI Yangiligi**\n\n📌 **{uzbekcha_sarlavha}**\n\n🔗 Batafsil o'qish (Manba): {link}\n\n@ai_uz_lab"
                    
                    counter += 1
                    maqola_rasmi = extract_image(entry, counter)
                    unikal_foto = f"{maqola_rasmi}&t={time.time()}"
                    
                    try:
                        bot.send_photo(chat_id=KANAL_USERNAME, photo=unikal_foto, caption=caption, parse_mode="Markdown")
                    except:
                        # Agar havola xato bo'lsa, zaxiradagi aniq ishlaydigan rasm bilan yuboramiz
                        zaxira_foto = f"{xilma_xil_rasmlar[counter % len(xilma_xil_rasmlar)]}&t={time.time()}"
                        bot.send_photo(chat_id=KANAL_USERNAME, photo=zaxira_foto, caption=caption, parse_mode="Markdown")
                    
                    yuborilgan_yangiliklar.add(link)
                    save_link(link)
                    print(f"Tarjima qilindi va yuborildi: {uzbekcha_sarlavha}")
                    break
            
            time.sleep(2)
                
    except Exception as e:
        print(f"Xato: {e}")
    
    time.sleep(30)