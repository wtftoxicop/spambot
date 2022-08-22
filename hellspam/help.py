from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5
from hellspam.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("Alive", b'alive'),
    Button.inline("Ping", b'ping')
], [
    Button.inline("Raid", b'raid'),
    Button.inline("Reply Raid", b'replyraid')
], [
    Button.inline("Spam", b'spam'),
    Button.inline("Porn Spam", b'pspam')
], [
    Button.inline("Extras", b'extras')
], [
    Button.url("Channel", "https://telegra.ph/file/0538467a48071262148fd.jpg"),
    Button.url("Group", "https://telegra.ph/file/0538467a48071262148fd.jpg")
]

BACK = [
    Button.inline("Back", b'back')
]

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/help'))

async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)
