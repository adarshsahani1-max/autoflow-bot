import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "नमस्ते! मैं आपका autoflow ऑटो-पोस्टिंग बॉट हूँ।\n"
        "मुझे अपने चैनल में Admin बनाएँ और पोस्ट ऑटोमेट करें।"
    )

if __name__ == '__main__':
    if not TOKEN:
        print("Error: BOT_TOKEN Environment Variable नहीं मिला!")
        exit(1)
        
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot चालू हो रहा है...")
    app.run_polling()
  
