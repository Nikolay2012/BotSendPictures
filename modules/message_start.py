import modules.bot as m_bot
import modules.keyboard_get_picture as m_key_get_picture
import modules.condition_send_picture as m_con_send_picture

@m_bot.bot.message_handler(commands=["start"])
def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id, # 
        "Hello, User!", #
        reply_markup = m_key_get_picture.keyboard_get_picture #
    )
    m_bot.bot.register_next_step_handler(
        message, 
        m_con_send_picture.condition_send_picture
    )