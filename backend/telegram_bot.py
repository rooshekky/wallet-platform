from telegram.ext import ApplicationBuilder, CommandHandler
import requests

API="https://your-api.up.railway.app"
TOKEN="BOT_TOKEN"

async def start(update,context):
    uid = update.effective_user.id
    requests.post(f"{API}/auth/telegram", json={"user_id":uid})
    await update.message.reply_text("Wallet created")

async def balance(update,context):
    uid = update.effective_user.id
    r=requests.get(f"{API}/wallet/{uid}")
    await update.message.reply_text(str(r.json()))

async def tip(update,context):
    await update.message.reply_text("Tip sent (demo)")

app=ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("balance",balance))
app.add_handler(CommandHandler("tip",tip))

app.run_polling()