import telegram
import asyncio

async def main():
    token = "6898150295:AAE8hxjfg3rQuGPzuEuwHPLNExqlZ3yAWKs"
    bot = telegram.Bot(token=token)
    public_chat_name = '@opensw2023'

    message = await bot.send_message(chat_id=public_chat_name, text="잘 안된다 그춍")
    id_channel = message.chat.id
    print(id_channel)

if __name__ == "__main__":
    asyncio.run(main())

