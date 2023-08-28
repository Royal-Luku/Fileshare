#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>I Am Permanent Royal FileStore Bot 🤖\n\nNot For All ❌ \nThis Bot Work Only For <a href='https://t.me/wombackup'>This Channel</a> If You Need A Bot Like Me Than DM My <a href='tg://user?id={OWNER_ID}'>Devoloper</a>! But it's Paid Not Free ! \n\n🤖 My Name: <a href='https://t.me/royalfilestorebot'>Rᴏʏᴀʟ FɪʟᴇSᴛᴏʀᴇ Bᴏᴛ</a>\n\n📝 Language: <a href='https://www.python.org'>Python 3</a>\n\n📚 Library:  <a href='https://docs.pyrogram.org'>Pyrogram</a>\n\n📡 Hosting Server : <a href='https://heroku.com'>Heroku</a>\n\n🧑🏻‍💻 Developer: <a href='tg://user?id={OWNER_ID}'>RoyalDwip</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
