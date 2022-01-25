from pyrogram import client, filters

Highlight=client(
    "Pyrogram bot",
    bot_token="5160356023:AAH_35hFryrGKFi_HCyLuJtFr0bf0zVxG1k",
    api_id="17827478",
    api_hash="22a35b5545535be40a1efae412b1b6b8"
)

@Highlight.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_text("hi")


Highlight.run()
