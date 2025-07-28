import os
import telebot
from flask import Flask, request

# Carga el token desde la variable de entorno
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_handler(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"""🚫 Hola {name}, No estás autorizado para usar este bot.

👤 Ow: @Dxniell777

🤖 MONITORING STATUS UPDATE 🤖
Hash 772.999
""")

@server.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def home():
    return "Bot activo."

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://tu-proyecto.railway.app/{TOKEN}")
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
