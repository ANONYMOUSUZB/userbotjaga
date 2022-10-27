from telethon import TelegramClient, events
from fayl.police import Online
import time
police = Online()
@events.register(events.NewMessage)
async def policehandler(event):
	        if ".police" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in police.online:
	        		time.sleep(0.3)
	        		await event.edit(d)