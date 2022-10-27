from telethon import TelegramClient, events, sync, functions, types
from telethon.errors import rpcbaseerrors
import time
##
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, aiocron, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User

import fayl.help
import fayl.loverun
import fayl.smilerun
import fayl.iloverun
import fayl.loveemojirun
import fayl.moonrun
import fayl.bombrun
import fayl.fuckrun
import fayl.snowrun
import fayl.lovelyrun
import fayl.UZBrun
import fayl.policerun
import fayl.brainrun
import fayl.ketdimrun
import fayl.kissrun
import fayl.magicrun


import fayl.client,fayl.help


client = fayl.client.client
botClient = fayl.client.botClient
@client.on(events.NewMessage(pattern=".test"))
async def _(event):
    await event.reply("ACCOUNT HACKED BY A.N.O.N.Y.M.O.U.S { CYBER AZROIL 👻 }")

with client as darknetos:
	 darknetos.add_event_handler(fayl.help.help)
with client as dark:
    dark.add_event_handler(fayl.loverun.lovehandler)
with client as smile:
    smile.add_event_handler(fayl.smilerun.smilehandler)
with client as ilove:
    ilove.add_event_handler(fayl.iloverun.ilovehandler)
with client as loveemoji:
    loveemoji.add_event_handler(fayl.loveemojirun.loveemojihandler)
with client as moon:
    moon.add_event_handler(fayl.moonrun.moonhandler)
with client as bomb:
    bomb.add_event_handler(fayl.bombrun.bombhandler)
with client as fuck:
    fuck.add_event_handler(fayl.fuckrun.fuckhandlers)
with client as snow:
    snow.add_event_handler(fayl.snowrun.snowhandler)
with client as lovely:
    lovely.add_event_handler(fayl.lovelyrun.lovelyhandler)
with client as dak:
    dak.add_event_handler(fayl.UZBrun.UZBhandler)
with client as police:
    police.add_event_handler(fayl.policerun.policehandler)
with client as dd:
     dd.add_event_handler(fayl.brainrun.brainhandler)
with client as bro:
    bro.add_event_handler(fayl.ketdimrun.ketdimhandler)
with client as bag:
    bag.add_event_handler(fayl.kissrun.kisshandler)
with client as dag:
    dag.add_event_handler(fayl.magicrun.magichandler)
    
    
    
    
    
client.start()
client.run_until_disconnected()