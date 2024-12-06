
# Telegram AI Bot

This is a Telegram bot that integrates multiple AI clients (OpenAI and MistralAI) to provide conversational responses. The bot allows you to switch between AI clients dynamically and offers helpful commands for interaction.

## Bot Details

- **Bot Name:** [practicebot](https://t.me/mypractice89_bot)
- **Username:** `@mypractice89_bot`

## Commands

| Command        | Description                                     |
| -------------- | ----------------------------------------------- |
| `/start`     | Starts the bot and sends a welcome message.     |
| `/help`      | Displays the help menu with available commands. |
| `/openai`    | Switches the bot to use the OpenAI client.      |
| `/mistralai` | Switches the bot to use the MistralAI client.   |
| `/clear`     | Clears the conversation history.                |

## How to Run the Bot

1. **Clone the Repository:**
   `git clone https://github.com/PoojaMaheshGori/telegram-ai-bot.git`
2. **Install Dependencies:** Use `pip` to install the required packages: `pip install -r requirements.txt`
3. **Set Up Environment Variables:**
   Create a `.env` file in the project directory with the following content:

```
    	TELEGRAM_BOT_TOKEN=your_telegram_bot_token
	OPENAI_API_KEY=your_openai_api_key
	MISTRAL_API_KEY=your_mistral_api_key
```

4. **Run the Bot:**
   Start the bot using the following command:
   `python my_bot.py`

## Dependencies

The project uses the following libraries:

- **[aiogram](https://docs.aiogram.dev/en/latest/):** For Telegram bot development.
- **openai:** For OpenAI client integration.
- **mistralai:** For MistralAI client integration.
- **dotenv:** For managing environment variables.

Install all dependencies via `requirements.txt`.

## Features

- **Dynamic AI Switching:** Use `/openai` or `/mistralai` to switch AI clients.
- **Conversation Memory:** Maintains context for better AI responses.
- **Clear Context:** Reset the conversation using `/clear`.

## Resources

- **Telegram Bot API Documentation:** [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api)
- **aiogram Documentation:** [https://docs.aiogram.dev/en/latest/](https://docs.aiogram.dev/en/latest/)

## Example Usage

1. Start the bot using `/start`.
2. Switch to OpenAI with `/openai` or MistralAI with `/mistralai`.
3. Send messages, and the bot will respond using the selected AI client.
4. Clear the context with `/clear` if needed.

## Troubleshooting

1. **Missing Dependencies:**Ensure all required packages are installed using:`pip install -r requirements.txt`
2. **Environment Variables Not Set:**Make sure the `.env` file exists and contains valid API keys.
3. **Permission Errors:**
   Run the bot with the necessary permissions or as an administrator.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
