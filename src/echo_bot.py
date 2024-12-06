from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging

load_dotenv()
api_key = os.getenv("TELEGRAM_BOT_TOKEN")
if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables or .env file.")
        
#configure logging
logging.basicConfig(level=logging.INFO)

#initialize the bot
bot = Bot(token=api_key)
dp = Dispatcher(bot)

# Graceful shutdown handler
async def on_shutdown(dispatcher: Dispatcher):
    print("Shutting down gracefully...")
    await bot.session.close()  # Close bot session

# Start command handler
@dp.message_handler(commands=["start"])
async def start_command(message):
    await message.reply("Hello! I am your bot.")
    
    

@dp.message_handler(commands=['info','help'])
async def command_start_handler(message: types.Message):
    """This handler receives messages with `/info` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi!\n I am an Echo Bot!\n Powered by Aiogram")

@dp.message_handler()
async def echo(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply(message.text)


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown)
    except Exception as e:
        print(f"Error occurred: {e}")
