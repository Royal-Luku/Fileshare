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
            text = f"<b>I Don't Know Why You Are Too Much Curious About To Knowing Me? \n\n 🤖 My Name: <a href='https://t.me/royalfilestorebot'>Rᴏʏᴀʟ FɪʟᴇSᴛᴏʀᴇ Bᴏᴛ</a>\n\n📝 Language: <a href='https://www.python.org'>Python 3</a>\n\n📚 Library:  <a href='https://docs.pyrogram.org'>Pyrogram</a>\n\n📡 Hosting Server : <a href='https://heroku.com'>Heroku</a>\n\n🧑🏻‍💻 Developer: <a href='tg://user?id={OWNER_ID}'>RoyalDwip</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("HOME", callback_data = "start")
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
