from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
from src.ai_client import OpenAIClient, MistralAIClient  # Import your AI client classes

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Fetch API tokens from environment
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not API_TOKEN:
    logging.error("Missing TELEGRAM_BOT_TOKEN in environment variables.")
    exit("Ensure all required environment variables are set.")

# Initialize AI client (can be replaced with other implementations later)
ai_client = MistralAIClient(api_key=os.getenv("MISTRAL_API_KEY"), model="mistral-large-latest")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)

# Conversation context
conversation_context = [{"role": "system", "content": "You are ahelpful assistant. Be patient and wait for the instructions. Give helpful replies to the questions."}]
    

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    Handler for the `/start` command.
    Sends a welcome message to the user.

    Args:
        message (types.Message): The incoming message object.
    """
    await message.reply("Hi there! 👋\nI'm a Chat Bot. How can I assist you today?")

@dispatcher.message_handler(commands=['help'])
async def display_help(message: types.Message):
    """
    Handler for the `/help` command.
    Displays a help menu with available commands.

    Args:
        message (types.Message): The incoming message object.
    """
    help_text = """
    **Help Menu** 🤖
    Available commands:
    - `/start`: Start the conversation.
    - `/clear`: Clear the current conversation and context.
    - `/help`: Display this help menu.
    - `/openai`: Choose openAI.
    - `/mistralai`: Choose MistralAI.

    How can I assist you? 😊
    """
    await message.reply(help_text, parse_mode="Markdown")

@dispatcher.message_handler(commands=['openai','mistralai'])
async def select_client(message: types.Message):
    """
    Handler for selecting the AI client based on the command.
    
    Args:
        message (types.Message): The incoming message object.
    """
    global ai_client  # Use a global variable to track the current client
    
    if message.text == "/openai":
        # Select OpenAI client
        ai_client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")
        await message.reply("OpenAI Client selected! 🎉\nHow can I assist you?")
    elif message.text == "/mistralai":
        # Select MistralAI client
        ai_client = MistralAIClient(api_key=os.getenv("MISTRAL_API_KEY"), model="mistral-large-latest")
        await message.reply("MistralAI Client selected! 🚀\nHow can I assist you?")
    else:
        await message.reply("Unknown command. Please use `/openai` or `/mistralai` to select the AI client.")

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    Handler for the `/clear` command.
    Clears the conversation context.

    Args:
        message (types.Message): The incoming message object.
    """
    # clear_context()
    global conversation_context
    conversation_context = [{"role": "system", "content": "You are a helpful assistant. Be patient and wait for the instructions. Give appropriate replies to the questions."}]
    await message.reply("All conversation context has been cleared. Let's start fresh! ✨")

@dispatcher.message_handler()
async def handle_message(message: types.Message):
    """
    Main handler for user messages.
    Processes user input using the currently selected AI client.
    """
    # global ai_client

    if ai_client is None:
        await message.reply("No AI client selected. Please use `/openai` or `/mistralai` to select an AI client.")
        return

    user_input = message.text

    try:
        # Generate response using the selected AI client
        conversation_context.append({"role": "user", "content": user_input})
        bot_response = ai_client.get_response(prompts=conversation_context)
        conversation_context.append({"role": "assistant", "content": bot_response})
        await bot.send_message(chat_id=message.chat.id, text=bot_response)
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        await message.reply("Sorry, I encountered an issue while processing your request. Please try again.")

if __name__ == "__main__":
    try:
        logging.info("Bot is starting...")
        executor.start_polling(dispatcher, skip_updates=True)
    except Exception as e:
        logging.critical(f"Critical failure: {e}")
