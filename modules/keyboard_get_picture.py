import modules.button_get_picture as m_bt_get_picture
import telebot

keyboard_get_picture = telebot.types.ReplyKeyboardMarkup()

keyboard_get_picture.add(m_bt_get_picture.button_get_picture)