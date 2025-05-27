import telebot
import random
import numpy as np
import matplotlib.pyplot as plt
from telebot import types
import requests
import io

# === ИНИЦИАЛИЗАЦИЯ БОТА ===
bot = telebot.TeleBot('7881527217:AAGBA5nuMc4xKT-Zrcq2DQS2QRIaXCyB9eM')

# === ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ===
user_data = {}
sticker_list = {
    'error': [
        'CAACAgIAAxkBAAEGqBNk4VuT9WzQlF57FNJr8VcZDRhx6gACGQMAApcRCQABvBBiOItmxS0E'
    ],
    'goida': [
        'CAACAgIAAxkBAAEPbZdoNah2TkYMJ5zOmlbY-tN2u3WE2AACVTgAAo7VSEnk8rF7Ppfl4DYE',
        'CAACAgIAAxkBAAEPbZpoNah4dzLmzsII4c9U4ZmYSB9BhQAC4DgAAvk8SUkmSGJ5cpWehjYE',
        'CAACAgIAAxkBAAEPbatoNaiuF-x7PnBn6v0LWlnK59MnkgACIUUAAuftOUovouGpr4g9TTYE',
        'CAACAgIAAxkBAAEPba9oNajgRUAnigW3N8Jr06oG-LxDiQACujgAAhWamUhZl9XlP0B72jYE',
        'CAACAgIAAxkBAAEPbbFoNajhoxxCSLiqAAEE9kJ2uTf_9KAAApw2AAIXlZhIq3dTRBsH2is2BA',
        'CAACAgIAAxkBAAEPbbNoNajjthkAAZQzBmfZRw_rpeOfYQIAAmE3AAJPU5hIQ1KdsO34a5g2BA',
        'CAACAgIAAxkBAAEPbbVoNajqw0s38fOHhpK5iG_ShkE2CQACJ0EAAtLtmUiaTTNVaeXe9DYE',
        'CAACAgIAAxkBAAEPbbdoNajtb_pg-bye1RnhfTT05KQi8QACzzAAAmFwmUgvXx78yPtIMzYE',
        'CAACAgIAAxkBAAEPbbtoNaj2wfRVyuf7j9TNF8VWV8q-pAAC7EIAAnRAeEnjPqBPVlaNozYE',
        'CAACAgIAAxkBAAEPbb1oNakFfATjYBSCngTWBUh6W4TDDgACOF4AAtRQOUkt1EPLU15JCTYE',
        'CAACAgIAAxkBAAEPbb9oNakICdQWfP7tg3Ohzmti93DQ-QACJl8AAsmZ4EoKF9dKGB8fhzYE',
        'CAACAgIAAxkBAAEPbcFoNakZKufRyfXlxmnkH4BZK2i6cQACzmkAAtMwwUqWjQ-MdSGzdjYE',
        'CAACAgIAAxkBAAEPbcNoNakk-k0Dh5kTaKBcrHyv97B9GAACiTAAAiVxmUss3g7F0lwxOjYE',
        'CAACAgIAAxkBAAEPbcdoNak5hsu5Q8lJxWu8ljAQJKmXPQACWj4AAtZH2UmCKTLLLzre-jYE',
        'CAACAgIAAxkBAAEPbcloNak-_HuWVNa_zjhoGPBQ7IwlTAAClmAAAp7OCwABqDDj2ubWhe02BA',
        'CAACAgIAAxkBAAEPbc9oNalru0a4E1hAdXRc3fRVcl71dwAChUsAAjbleUlcxsYI4vfRQzYE',
        'CAACAgIAAxkBAAEPbdNoNamYKUhuYTNRvHKbRejc-y3onwAC6yAAAngg2EtLS_myhZ_uczYE',
        'CAACAgIAAxkBAAEPbdVoNamjzEZ0zCz-UpjHI4419RraqgACbR0AArIZ2Us0bhai2DBsszYE',
        'CAACAgIAAxkBAAEPbddoNamrpdSWAd71v_SgHRqbSAyF5wAC9ScAAnlG0EvKqZuxod0ptTYE',
        'CAACAgIAAxkBAAEPbd9oNanZtFCx4N3jN3Z0ulMsoNTj3gACFzQAAvkpOEs8u7UZaS_N-zYE',
        'CAACAgIAAxkBAAEPbeFoNanbw098je5SEwkJdYBuUjlAGgACSTMAAusFOUv9cUMINfIw6DYE',
        'CAACAgIAAxkBAAEPbeNoNancXR9xhde33J8y_NRi85U3JgACUjMAAkqwOUtxs9V5Kdl0cDYE',
        'CAACAgIAAxkBAAEPbetoNaoNZ0rrGzuQ1CKTVTGOJGbRwgAC6ikAAlgRyEpL-3-6K3xu2zYE',
        'CAACAgIAAxkBAAEPbe9oNaocwzs03u3A20MyhH_W7WIsgwACqlYAAl5bCEnZrqW7iCmdgzYE',
        'CAACAgIAAxkBAAEPbfFoNaouyrbCRwVANwVkQu40-Mw8jwACHysAAl39yEr-qR83tAJMVjYE',
        'CAACAgIAAxkBAAEPbfNoNao86X1-84JfF143QP_Tnb6aKwACzhYAAi_J6Ek6q3zfiAtqDjYE',
        'CAACAgIAAxkBAAEPbfVoNapHZhdqwqQubO6vNo5H4n_1uAACOyIAAr7maUv7VPeYre_DojYE',
        'CAACAgIAAxkBAAEPbgJoNaswPo4DYJH6UwOxezaTNqG_3QAC9C0AAnsrwEmLPHbDg_W8YTYE',
        'CAACAgIAAxkBAAEPbgRoNatD7qH0zgHkpyrx1ozwkNGWjgACQBUAAsvQKEhYAvM4TJrDvzYE'
    ]
}

# === КНОПКИ ===
def make_buttons():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Погода')
    btn2 = types.KeyboardButton('Стикеры')
    btn3 = types.KeyboardButton('График')
    btn4 = types.KeyboardButton('Помощь')
    buttons.add(btn1, btn2, btn3, btn4)
    return buttons

# === ПОГОДА ===
def city(message):
    msg = bot.send_message(message.chat.id, "Напиши город:")
    bot.register_next_step_handler(msg, weather)

def weather(message):
    try:
        city = message.text.strip()
        print("Пользователь ввёл:", city)

        if city.lower() in ['погода', 'привет', 'график', 'стикеры', 'помощь']:
            bot.send_message(message.chat.id, "Вы снова выбрали команду. Сначала введите название города.")
            city(message)
            return

        api_key = "2e63eacbfb720893b10d56926a52c88a"  
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}'
        response = requests.get(url)
        data = response.json()

        print("Статус код:", response.status_code)
        print("Ответ от API:", data)

        if data['cod'] == 200:
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            bot.send_message(message.chat.id,
                            f"Погода в {city}:\n{weather_desc}\nТемпература: {temp}°C\nОщущается как: {feels_like}°C")
        else:
            error_msg = data.get('message', 'Неизвестная ошибка')
            bot.send_message(message.chat.id, f"Ошибка: {error_msg}. Попробуйте другой город.")
            city(message)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при получении погоды: {e}")
        city(message)

# === СТИКЕРЫ ===
def send_sticker(chat_id):
    all_stickers = []
    for v in sticker_list.values():
        all_stickers += v
    bot.send_sticker(chat_id, random.choice(all_stickers))

# === ПОМОЩЬ ===
def show_help(message):
    bot.send_message(message.chat.id,
                    "Что я умею:\n/start - начать\nПогода - узнать погоду\nСтикеры - получить стикер\nГрафик - построить график")

# === ГРАФИК ===
def ask_for_numbers(message):
    msg = bot.send_message(message.chat.id, "Введи три числа через пробел для уравнения y = k1*x² + k2*x + k3:")
    bot.register_next_step_handler(msg, get_numbers)

def get_numbers(message):
    try:
        numbers = list(map(float, message.text.split()))
        if len(numbers) != 3:
            raise ValueError

        user_data[message.chat.id] = numbers
        draw_graph(message.chat.id)

    except:
        bot.send_message(message.chat.id, "Неправильный ввод. Нужно три числа через пробел, например: 1 -2 3")
        bot.send_sticker(message.chat.id, random.choice(sticker_list['error']))
        ask_for_numbers(message)

def draw_graph(chat_id):
    try:
        k1, k2, k3 = user_data[chat_id]

        x = np.linspace(0, 100, 400)
        y = k1 * x ** 2 + k2 * x + k3

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, color='blue')
        plt.title(f'График: y = {k1}x² + {k2}x + {k3}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        bot.send_photo(chat_id, img)
        plt.close()

    except Exception as e:
        bot.send_message(chat_id, f"Ошибка: {str(e)}")
        bot.send_sticker(chat_id, random.choice(sticker_list['error']))

# === ОБРАБОТЧИКИ ===
@bot.message_handler(commands=['start'])
def cmd_start(message):
    try:
        with open('img.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Привет, человек", reply_markup=make_buttons())
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка загрузки изображения.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text

    if text == 'Привет':
        try:
            with open('img.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption="Привет, человек", reply_markup=make_buttons())
        except Exception as e:
            bot.send_message(message.chat.id, "Ошибка загрузки изображения.")

    elif text == 'Погода':
        city(message)

    elif text == 'Стикеры':
        send_sticker(message.chat.id)

    elif text == 'График':
        ask_for_numbers(message)

    elif text == 'Помощь':
        show_help(message)

    else:
        bot.send_message(message.chat.id, "Напиши /start или выбери команду с клавиатуры.")

# === ЗАПУСК БОТА ===
print("Бот запущен...")
bot.polling(none_stop=True, interval=0)