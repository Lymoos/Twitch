from aiogram import Bot, Dispatcher,types,F
from aiogram.types import Message
import asyncio
from aiogram.enums import ParseMode
from aiogram.filters import Command

#strart funcs
bot = Bot(token="6731730299:AAHNrGAQfiU5BJzoxmV9ftuslKWZMjdFHkc")
dp = Dispatcher()
#programm
@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
    f"Hello, <b>{message.from_user.full_name}</b>",
    parse_mode=ParseMode.HTML
    )

async def main_telegram():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main_telegram())