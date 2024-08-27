from aiogram import types, Dispatcher
from utils import get_or_create_alias, add_user, get_all_users

async def handle_message(message: types.Message):
    # Регистрируем пользователя и получаем его псевдоним
    user_id = message.from_user.id
    add_user(user_id)
    alias = get_or_create_alias(user_id)
    text = f"{alias}: {message.text}"

    # Получаем всех пользователей и отправляем им сообщение, кроме отправителя
    users = get_all_users()
    for recipient_id in users:
        if recipient_id != user_id:
            try:
                await message.bot.send_message(chat_id=recipient_id, text=text)
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {recipient_id}: {e}")

def register_handlers(dp: Dispatcher):
    dp.message.register(handle_message)
