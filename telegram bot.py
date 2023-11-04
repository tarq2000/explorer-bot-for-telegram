import telebot
from telebot import types

# Replace with your bot's API token
API_TOKEN = 'YOUR_API_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

selected_language = {}
# Define custom keyboard buttons in different languages
languages_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
russian_button = types.KeyboardButton("Русский")
english_button = types.KeyboardButton("English")
arabic_button = types.KeyboardButton("عربی")
persian_button = types.KeyboardButton("فارسی")
languages_keyboard.row(russian_button, english_button, arabic_button, persian_button)


language_options = {
    "Русский": [
        ["Button1", "Button2", "Button3", "Button4"],
        [
            "https://t.me/rian_ru",
            "https://t.me/tass_agency",
            "https://t.me/roscosmos_gk",
            "https://t.me/oleg_mks",
        ],
    ],
    "English": [
        ["Button1", "Button2", "Button3", "Button4"],
        [
            "https://t.me/BBCWorldoffl",
            "https://t.me/SpaceX",
            "https://t.me/SpaceX",
            "https://t.me/SpaceX",
        ],
    ],
    "عربی": [
        ["Button1", "Button2", "Button3", "Button4"],
        [
            "https://t.me/rian_ru",
            "https://t.me/tass_agency",
            "https://t.me/roscosmos_gk",
            "https://t.me/oleg_mks",
         ],
    ],
    "فارسی": [
        ["Button1", "Button2", "Button3", "Button4"],
        [
            "https://t.me/rus_cosmos",
            "https://t.me/rus_cosmos",
            "https://t.me/rus_cosmos",
            "https://t.me/bbcpersian",
        ],
    ],
}
@bot.message_handler(commands=['start'])
def send_language_select(message):
    bot.send_message(message.chat.id, "Choose your language:", reply_markup=languages_keyboard)

@bot.message_handler(func=lambda message: message.text in language_options)
def set_selected_language(message):
    selected_language[message.chat.id] = message.text
    language = message.text
    buttons = language_options[language][0]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        keyboard.add(types.KeyboardButton(button))
    bot.send_message(message.chat.id, "Choose a channel:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in sum([lang[0] for lang in language_options.values()], []))
def send_channel_posts(message):
    chat_id = message.chat.id
    language = selected_language.get(chat_id)
    if language:
        channel_index = language_options[language][0].index(message.text)
        channel_url = language_options[language][1][channel_index]
        # Fetch and display the 10 latest posts from the channel URL. Replace this with your post fetching logic.
        bot.send_message(chat_id, f"Fetching and displaying posts from {channel_url}")

# Listen for messages and events
bot.polling()
