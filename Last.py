import telebot

token="5965343111:AAG0kU6vzfygxVGOAyDrpFy9B2JyOJOrZWk"
bot=telebot.Telebot(token)

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(messange.chat.id, 'Если тебе плохо')

@bot.messange_handler(content_types=["text"])
 def handler_text(message):bot.send_message(message.chat.id, 'ты можешь сказать мне про все свои проблемы!'+ message.text))
bot.polling()
