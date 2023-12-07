import telegram
import asyncio

async def main():
    token = "6898150295:AAE8hxjfg3rQuGPzuEuwHPLNExqlZ3yAWKs" 
    bot = telegram.Bot(token=token)
    chat_id = "6905523486" 
    text = "중성마녀 같다"

    await bot.send_message(chat_id=chat_id, text=text)

if __name__ == "__main__":
    asyncio.run(main())