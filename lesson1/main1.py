from aiogram import Bot, Dispatcher, executor, types

# бот-сервер ,который будет взоимодействия с API Telegram.
TOKEN_API = "6588785867:AAE-DM1CjiQOgQ00lnbC6T_9XIlNOhELU00"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text.upper())

if __name__ == '__main__':
    executor.start_polling(dp)
