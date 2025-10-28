import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import pytesseract
import cv2
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv() 


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

user_state = {}

button1 = InlineKeyboardButton(text='تبدیل عکس🖼️ به متن📄',callback_data='تبدیل عکس به متن')
btn_back = InlineKeyboardButton(text='🔙 بازگشت به منو', callback_data='back')

inline_keyword = InlineKeyboardMarkup(row_width=1)
inline_keyword.add(button1)



@bot.message_handler(commands=['start'])
def welcome(masage):
    bot.send_message(masage.chat.id, 'سلام خوش آمدید به ocr_bot', reply_markup=inline_keyword)


@bot.callback_query_handler()
def check_butten(call):
    if call.data == 'تبدیل عکس به متن':
        bot.send_message(call.message.chat.id, 'لطفا عکس خود را بفرستید')
        user_state[call.message.chat.id] = 'ocr'



@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    state = user_state.get(message.chat.id)

    if state == "ocr":
        # تبدیل عکس به متن
        try:
            file_info = bot.get_file(message.photo[-1].file_id)
            photo_data = bot.download_file(file_info.file_path)
            img = cv2.imdecode(np.frombuffer(photo_data, np.uint8), cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.medianBlur(img, 3)
            imag_to_text = pytesseract.image_to_string(img, lang='fas+eng+ara').strip()
            if imag_to_text:
                bot.reply_to(message, f"📄 متن استخراج‌شده:\n\n{imag_to_text}")
            else:
                bot.reply_to(message, "❌ متنی برای استتخراج در تصویر پیدا نشد.")
        except Exception as e:
            bot.reply_to(message, f"⚠️ خطا در پردازش تصویر:\n{e}")
     


bot.polling(skip_pending=True)