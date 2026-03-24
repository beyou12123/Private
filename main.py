import asyncio
from telethon import TelegramClient

# --- بياناتك الخاصة ---
api_id = 20443064
api_hash = '061a4fa5feffd11330bcc62ce0dd65cc'

# --- قائمة البوتات المستهدفة ---
target_bots = ['@Uploadfilesmnbot', '@Ghhggggffdfgggbot']

async def main():
    print("🔄 جاري الاتصال بتليجرام... انتظر ظهور طلب الرقم")
    
    # إنشاء الجلسة باسم my_session
    client = TelegramClient('my_session', api_id, api_hash)
    
    # البدء وطلب الرقم والكود (هذا السطر سيفتح واجهة الإدخال)
    await client.start()
    
    print("✅ تم تسجيل الدخول بنجاح! البوت بدأ العمل...")
    
    while True:
        for bot in target_bots:
            try:
                # إرسال أمر /start للبوتات
                await client.send_message(bot, '/start')
                print(f"🚀 تم إرسال /start إلى {bot}")
            except Exception as e:
                print(f"❌ خطأ أثناء الإرسال لـ {bot}: {e}")
        
        # الانتظار لمدة 5 دقائق (300 ثانية)
        print("🕒 الدورة انتهت.. سأنتظر 5 دقائق قبل الإرسال القادم.")
        await asyncio.sleep(300)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 تم إيقاف البوت يدوياً.")
