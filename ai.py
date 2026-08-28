import time
import telebot

TELEGRAM_TOKEN = "8842296802:AAE78Gl1ReMvnR-F46TBTc6ATAmDE15CYKM"
KANAL_USERNAME = "@ai_uz_lab"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
print("Ultra Pro Max kengaytirilgan bot ishga tushdi...")

# Kengaytirilgan va uzunroq matnga ega postlar bazasi
postlar = [
    {
        "photo": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1000&auto=format&fit=crop",
        "caption": "💻 **Dars 1: Python'da O'zgaruvchilar va Ma'lumotlar Turlari**\n\nAssalomu alaykum qadrli kanalimiz a'zolari! Bugundan boshlab sizlar bilan noldan boshlab Python dasturlash tilini o'rganishni boshlaymiz.\n\n📌 **O'zgaruvchi nima?**\nO'zgaruvchi — bu kompyuter xotirasida ma'lum bir qiymatni saqlash uchun mo'ljallangan quti.\n\n🔹 Matnlar uchun: `str` (string)\n🔹 Butun sonlar uchun: `int` (integer)\n🔹 Kasr sonlar uchun: `float` (floating point)\n\nKeyingi darslarda amaliy mashqlarni ko'rib chiqamiz. Kanalimizdan uzoqlashmang! 🚀\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop",
        "caption": "🤖 **IT Yangilik: Sun'iy Intellekt olamidagi so'nggi yangiliklar**\n\nBugungi kunda sun'iy intellekt texnologiyalari shiddat bilan rivojlanmoqda. Har kuni yangidan-yangi neyrotarmoqlar taqdim etilmoqda.\n\n💡 **Asosiy o'zgarishlar:**\n• Dasturlash kodlarini yozish tezligi sun'iy intellekt yordamida 2 barobar oshdi.\n• Matn va tasvir generatorlari yanada aniqroq ishlay boshladi.\n• O'zbek tilidagi modellarning sifati kundan-kunga yaxshilanmoqda.\n\nTexnologiya ortda qolmaslik uchun har kuni yangiliklarni biz bilan kuzatib boring! 📈\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1000&auto=format&fit=crop",
        "caption": "⚡️ **Amaliy Qo'llanma: Telegram Bot qanday yaratiladi?**\n\nO'z Telegram botingizni yaratishni o'ylayapsizmi? Bu unchalik qiyin emas!\n\n🛠 **Kerakli qadamlar:**\n1. Telegram'da `@BotFather` orqali yangi bot ochib, Token olish.\n2. Python tilida `pyTelegramBotAPI` kutubxonasini o'rnatish.\n3. Xabarlarni qabul qilish va ularga javob qaytarish mantiqini yozish.\n\nTez orada botni noldan qanday yozish bo'yicha video va matnli darslarni tashlaymiz! 🔥\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=1000&auto=format&fit=crop",
        "caption": "🎯 **Pro Prompt: Sun'iy Intellektdan unumli foydalanish sirlari**\n\nChatGPT yoki Claude bilan ishlaganda to'g'ri buyruq (prompt) berish juda muhim. \n\n✍️ **Sifatli prompt tuzish formulasi:**\n• **Rol:** 'Sen tajribali dasturchisan'\n• **Vazifa:** 'Menga ushbu xatoni to'g'rilashga yordam ber'\n• **Kontekst:** 'Kod quyidagicha...'\n• **Format:** 'Javobni qisqacha va kod misoli bilan tushuntir'\n\nUshbu usuldan foydalanib ko'ring, natijasi sizni hayratda qoldiradi! 🧠\n\n@ai_uz_lab"
    },
    {
        "photo": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?q=80&w=1000&auto=format&fit=crop",
        "caption": "🌐 **Web Dars: HTML va CSS asoslari**\n\nHar qanday veb-saytning asosi bu HTML va CSS hisoblanadi.\n\n🧱 **HTML** — saytning skeleti (matnlar, rasmlar, havolalar).\n🎨 **CSS** — saytning ko'rinishi (ranglar, dizayn, joylashuv).\n\nAgar veb-dizayn yoki dasturlashga qiziqsangiz, aynan shu ikki tildan boshlash tavsiya etiladi.\n\nKanalimizda yaqin kunlarda veb-darslar boshlanadi! 🎨\n\n@ai_uz_lab"
    }
]

index = 0

while True:
    try:
        current_post = postlar[index % len(postlar)]
        
        bot.send_photo(
            chat_id=KANAL_USERNAME, 
            photo=current_post["photo"], 
            caption=current_post["caption"], 
            parse_mode="Markdown"
        )
        print(f"Kengaytirilgan post {index + 1} muvaffaqiyatli yuborildi!")
        
        index += 1
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    
    # 30 sekunddan keyin navbatdagi uzun va qiziqarli postni yuboradi
    time.sleep(10)