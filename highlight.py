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
Text = """
​╔════❰ ꪖ᥇ꪮꪊ𝓽 ꪑ𝘴ᧁ ❱═❍⊱❁۪۪ 
 ​║╭━━━━━━━━━━━━━━━➣  
 ​║┣⪼ 𝙈𝙔 𝙉𝘼𝙈𝙀 - <a href="https://t.me/HTTESTPYRO_BOT"> PYROBOT</a> 
║┣⪼ DEV - <a href="https://t.me/iTOMMYSHELBY"> TOMMY SHELBY </a> 
 ​║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 
 ​║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹 
 ​║┣⪼ 𝓓𝓪𝓽𝓪 𝓑𝓪𝓼𝓮 - 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱 
 ​║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 -  𝙷𝙴𝚁𝙾𝙺𝚄 
 ​║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v1.0.1 [ 𝙱𝙴𝚃𝙰 ] 
 ​║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪"""
"""
    await message.reply_photo(
        photo="https://telegra.ph/file/6f014e3d6c8b90cb6d49e.jpg",
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
   

@Highlight.on_message(filters.command("info"))
async def info_message(bot, messege):
    text = f"""
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
