import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from bot_func import get_token_env
from file_path import path_to_webp_image

bot = Bot(get_token_env())
dp = Dispatcher()


@dp.message()
async def echo_message(message: types.Message):
    photo_obj = types.input_file.FSInputFile(path=path_to_webp_image)
    await message.answer_photo(photo=photo_obj)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
