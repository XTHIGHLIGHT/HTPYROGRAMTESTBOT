from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Highlight=Client(
    "Pyrogram bot",
    bot_token="5071694006:AAGIeZuN6F_31aEW-PE-lNr4bRjq26rA4HM",
    api_id="17827478",
    api_hash="22a35b5545535be40a1efae412b1b6b8"
)

@Highlight.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/6f014e3d6c8b90cb6d49e.jpg",
        caption="♻️JOIN OUR CHANNELLS TO GET LATEST MOVIES♻️",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton ("✳️MAIN CHANNEL✳️", url="https://t.me/+RoU6VdIQ719iMDVl"),
            InlineKeyboardButton ("✳️CHANNEL 2.0✳️", url="https://t.me/+gDbr4bXrylZjNjJl")
            ],[
            InlineKeyboardButton ("✳️GROUP✳️", url="https://t.me/+82wh0nsgECRhODM1")
            ]]
            )
        )
    
   
        
        
        


@Highlight.on_message(filters.command("help")) 
async def help(bot: Highlight, message: Message):
    await message.reply_text("https://youtu.be/Af055Eozk9s")


Highlight.run()
