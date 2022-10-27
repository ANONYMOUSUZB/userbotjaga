from telethon import TelegramClient, events
from fayl.ketdim import Online
import time
ketdim = Online()
@events.register(events.NewMessage)
async def ketdimhandler(event):
	        if ".ketdim" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in ketdim.online:
	        		time.sleep(0.3)
	        		await event.edit(d)