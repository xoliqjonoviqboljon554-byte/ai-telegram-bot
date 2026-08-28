import time
import telebot
import google.generativeai as genai

# Token va kalitni to'g'ridan-to'g'ri shu yerga yozamiz
TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
GEMINI_API_KEY = "AQ.Ab8RN6JGXf9FsO_tKYj_B_3FYx7UikrF715i9VTZiipm-T2bQQ"
KANAL_USERNAME = "@ai_uz_lab"

# Gemini va Telegram botni sozlash
genai.configure(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

print("Bot ishga tushdi va har 10 sekundda post yuborishni boshladi...")

while True:
    try:
        # Yangi va barqaror model nomini ishlatamiz
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = "Telegram kanali uchun qiziqarli, qisqa va foydali bitta gapli fakt yoki motivatsiya yozib ber (o'zbek tilida)."
        response = model.generate_content(prompt)
        
        post_matni = response.text
        
        bot.send_message(KANAL_USERNAME, post_matni)
        print("Post muvaffaqiyatli yuborildi!")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    
    time.sleep(10)