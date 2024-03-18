from telebot import TeleBot, types
import sqlite3

bot = TeleBot("ваш_токен_бота")  # замените "ваш_токен_бота" на токен вашего бота

def get_user_data(user_id):
    conn = sqlite3.connect("users.db")  # замените "users.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data

def set_user_data(user_id, data):
    conn = sqlite3.connect("users.db")  # замените "users.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, data) VALUES (?, ?)", (user_id, data))
    conn.commit()
    conn.close()

@bot.message_handler(commands=["start"])
def start_command(message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)
    if user_data is None:
        set_user_data(user_id, {"name": message.from_user.first_name})  # замените "name" на имя поля, в которое нужно сохранить имя пользователя
    bot.send_message(message.chat.id, "Привет! Я бот, который может...")

@bot.message_handler(content_types=["text"])
def text_command(message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)
    if message.text == "/start":
        start_command(message)
    else:
        bot.send_message(message.chat.id, "Я не понимаю вашего сообщения.")

bot.polling()