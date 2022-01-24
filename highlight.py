from pyrogram import client, filters

Highlight=client(
    "Pyrogram bot",
    bot_token="5228659986:AAH93K7xVMwThS_u1FUaq6pN1govoq6wZQQ",
    api_id="17827478",
    api_hash="22a35b5545535be40a1efae412b1b6b8"
)

@Highlight.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_text("hi")


Highlight.run()
