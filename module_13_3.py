import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart


bot = Bot(token='')
dp = Dispatcher()
router = Router()


@router.message(CommandStart())
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@router.message()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
