import time
import telebot
import google.generativeai as genai

# Token va kalitingizni yozing
TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
GEMINI_API_KEY = "AQ.Ab8RN6JGXf9FsO_tKYj_B_3FYx7UikrF715i9VTZiipm-T2bQQ"
KANAL_USERNAME = "@ai_uz_lab"

# Gemini va Telegram botni sozlash
genai.configure(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

print("Bot ishga tushdi va dars hamda yangiliklarni yuborishni boshladi...")

# Dars va Yangiliklarni navbatma-navbat yuborish uchun mavzular
mavzular = [
    "Telegram kanali uchun Python yoki Sun'iy intellekt bo'yicha tushunarli, qisqa va foydali dars yozib ber (o'zbek tilida).",
    "IT olamidagi eng so'nggi yangiliklar yoki texnologik trendlar haqida qiziqarli post yozib ber (o'zbek tilida)."
]

index = 0

while True:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Navbatdagi mavzuni tanlaymiz (dars yoki yangilik)
        prompt = mavzular[index % len(mavzular)]
        response = model.generate_content(prompt)
        
        post_matni = response.text
        
        # Kanalga yuborish
        bot.send_message(KANAL_USERNAME, post_matni)
        print("Dars/Yangilik muvaffaqiyatli yuborildi!")
        
        index += 1
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    
    # Qancha vaqtda bir borishini shu yerda o'zgartirishingiz mumkin (masalan: 30 sekund yoki 60 sekund)
    time.sleep(30)