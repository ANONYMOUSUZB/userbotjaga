from telethon import TelegramClient, events
import fayl.client
from fayl.fuck import Fuck
import time
fuck = Fuck()
client = fayl.client.client
@events.register(events.NewMessage)
async def fuckhandlers(event):
		for i in range(3):
					if '.fuck' in event.raw_text:
						time.sleep(0.3)
						for d in fuck.fuck:
							time.sleep(0.3)
							await event.edit(d)