from telethon import TelegramClient, events
from fayl.UZB import Online
import time
UZB = Online()
@events.register(events.NewMessage)
async def UZBhandler(event):
	        if ".uzb" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in UZB.online:
	        		time.sleep(0.3)
	        		await event.edit(d)