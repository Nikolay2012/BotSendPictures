import modules.bot as m_bot

def condition_send_picture(message):
    if message.text.lower() == "get picture":
        m_bot.bot.send_photo(
            message.chat.id, 
            "https://klike.net/uploads/posts/2019-11/1574514215_2.jpg"
        )
    m_bot.bot.register_next_step_handler(message, condition_send_picture)


