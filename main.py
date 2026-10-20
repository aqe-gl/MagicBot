import telebot
import random

bot = telebot.TeleBot('8934757583:AAF5WzvVOMnDbDp0n6BwSj1CMzLvfDkX3vU')

answers = [
    "Yes",
    "No",
    "I don't know",
    "Of course",
    "Don't think about it",
    "Listen to your heart on this one"
]

@bot.message_handler(commands=['start'])
def start(message):
    print("Start")
    bot.reply_to(message, "Hello! I'm a bot.")

@bot.message_handler(commands=['hello', 'hi'])
def greeting(message):
    bot.reply_to(message, "Glad to see you.")

@bot.message_handler(commands=['stop', 'bye'])
def stop(message):
    bot.reply_to(message, "Goodbye.")

@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text
    if "?" in text:
        bot.reply_to(message, f"My answer: {random.choice(answers)}")
    else:
        bot.reply_to(message, f"Ask me a question and I'll answer.")


bot.polling(non_stop=True, interval=0)