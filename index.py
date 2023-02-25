import os
import openai
import telebot

TOKEN = os.environ.get('TOKEN', None)
openai.api_key = os.environ.get('OPENAI', None)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    #print(message.text)
    response = openai.Completion.create(
    model="text-davinci-003",
      prompt=message.text,
      temperature=0.9,
      max_tokens=150,
      user="1",
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6
    )
    #print(response['choices'][0]['text'])
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.polling()
