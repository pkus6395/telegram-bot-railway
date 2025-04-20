
import os
import asyncio
import random
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from datetime import datetime

TOKEN = os.getenv('BOT_TOKEN')  # ใช้ Token จาก Environment Variables

app = ApplicationBuilder().token(TOKEN).build()

# รายชื่อข้อความสุ่ม
messages = [
    "🔥 โปรโมชั่นใหม่! สมัครรับโบนัสทันที!",
    "🎯 คาสิโนสด ฝากถอนไว ไม่ง้อเอเย่นต์!",
    "🎰 สล็อตแตกง่าย 2025 เล่นได้ทุกวัน!",
]

# ชั่วโมงที่ต้องยิงข้อความ
post_hours = [10, 14, 20]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ สวัสดีครับ ยินดีต้อนรับสู่ Casino168!")

# ตอบข้อความทั่วไป
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ รับข้อความแล้วครับ!")

# ฟังก์ชันยิงข้อความตามเวลา
async def send_random_message(context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    if now.hour in post_hours:
        selected_message = random.choice(messages)
        try:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=selected_message)
            print(f"✅ ยิงข้อความ: {selected_message} ({now.strftime('%H:%M')})")
        except Exception as e:
            print(f"❌ ยิงล้มเหลว: {e}")

if __name__ == '__main__':
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, reply_message))
    app.job_queue.run_repeating(send_random_message, interval=60, first=10)
    app.run_polling()
