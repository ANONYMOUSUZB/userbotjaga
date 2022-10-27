from telethon import TelegramClient, events
import fayl.client
from fayl.magic import Magic
import time
magic = Magic()
client = fayl.client.client
@events.register(events.NewMessage)
async def magichandler(event):
		if '.magic' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)