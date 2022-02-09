from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Highlight=Client(
    "Pyrogram bot",
    bot_token="5071694006:AAGIeZuN6F_31aEW-PE-lNr4bRjq26rA4HM",
    api_id="17827478",
    api_hash="22a35b5545535be40a1efae412b1b6b8"
)

START_MESSAGE = """
Hello {}
"""

@Highlight.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/6f014e3d6c8b90cb6d49e.jpg",
    await message.reply_text(
        text=START_MESSAGE.format(message.from_user.mention)
    )
   

@Highlight.on_message(filters.command("info"))
async def info(bot, messege):
    text = """
First Name - {message.from_user.first_name}
Last Name - {message.from_user.last_name}
UserName - {message.from_user.username}
Id - {message.from_user.id}
Mention - {message.from_user.mention}"""

    await message.reply_text(text=text)
        
        
@Highlight.on_message(filters.command("help")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/6f014e3d6c8b90cb6d49e.jpg",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton ("CLICK HERE", url="https://youtu.be/Af055Eozk9s")
            ]]
            )
        )


Highlight.run()
