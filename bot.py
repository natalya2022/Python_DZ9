from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from game import *

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("go", toss_command))
app.add_handler(MessageHandler(filters.TEXT, game_command))

print('start')
app.run_polling()