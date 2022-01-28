from pyrogram import Client, filters
from pyrogram.types import Message

Highlight=Client(
    "Pyrogram bot",
    bot_token="5071694006:AAGIeZuN6F_31aEW-PE-lNr4bRjq26rA4HM",
    api_id="17827478",
    api_hash="22a35b5545535be40a1efae412b1b6b8"
)

@Highlight.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_text("Hi I am Adrin and I am trying to become a developer with Motech")


@Highlight.on_message(filters.command("help")) 
async def help(bot: Highlight, message: Message):
    await message.reply_text("CONTACT:@iamAdrin")


Highlight.run()
