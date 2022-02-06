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
        caption="⭕JOIN TO GET LATEST MOVIES⭕",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton ("MYTHRI MOVIES", url="https://t.me/MythriMovies"),
            InlineKeyboardButton ("MM LINKZ", url="https://t.me/MMlinkz")
            ],[
            InlineKeyboardButton ("MMSUPPORTTGROUP", url="https://t.me/MMsupporttgroup"),
            InlineKeyboardButton ("MMOFCGROUP", url="https://t.me/MMofcgroup")
            ],[
            InlineKeyboardButton ("DEV🧑‍💻", url="https://t.me/iTOMMYSHELBY"),
            InlineKeyboardButton ("Repository🤖", url="https://github.com/XTHIGHLIGHT")
            ]]
            )
        )
    
   
        
        
        
@Highlight.on_message(filters.command("help")) 
async def help(bot: Highlight, message: Message):
    await message.reply_text("https://youtu.be/Af055Eozk9s")


Highlight.run()
