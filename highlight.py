from pyrogram import Client, filters

Highlight=Client(
    "Pyrogram bot",
    bot_token="5168351626:AAFFXbP3s514IKZ8qcE6qXFOqmxCXGAb0BM",
    api_id="17827478",
    api_hash="22a35b5545535be40a1efae412b1b6b8"
)

@Highlight.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_text("hi")


Highlight.run()
