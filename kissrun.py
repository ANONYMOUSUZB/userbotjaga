from telethon import TelegramClient, events
from fayl.kiss import Online
import time
kiss = Online()
@events.register(events.NewMessage)
async def kisshandler(event):
	        if ".kiss" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in kiss.online:
	        		time.sleep(0.3)
	        		await event.edit(d)