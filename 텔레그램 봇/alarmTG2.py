import telegram
import asyncio
import schedule
import time
import pytz
import datetime

async def send_telegram_message():
    token = "6898150295:AAE8hxjfg3rQuGPzuEuwHPLNExqlZ3yAWKs"
    bot = telegram.Bot(token = token)
    public_chat_name = '@opensw2023'
    message = await bot.send_message(chat_id=public_chat_name, text="알람 도착")
    id_channel = message.chat.id
    print(id_channel)

def job():
    now = time.localtime()
    print("현재시간 =",str(now))
    
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
