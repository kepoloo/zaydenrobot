from pyrogram import filters
from blackpink import blackpink as bp
from AvishaRobot import pbot as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/ZaydenStreamBot?startgroup=true"),
    ],
]

###
@app.on_message(filters.command("blackpink"))
async def blackpink(_, message):
    text = message.text[len("/blackpink ") :]
    bp(f"{text}").save(f"blackpink_{message.from_user.id}.png", caption=f"❖ ʙʟᴀᴄᴋᴘɪɴᴋ ʙʏ ➥ ˹𝙕𝙖𝙮𝙙𝙚𝙣 ✘ 𝙅𝙤𝙤𝙭 🎧˼", reply_markup=InlineKeyboardMarkup(EVAA),)
    await message.reply_photo(f"blackpink_{message.from_user.id}.png", caption=f"❖ ʙʟᴀᴄᴋᴘɪɴᴋ ʙʏ ➥ ˹𝙕𝙖𝙮𝙙𝙚𝙣 ✘ 𝙅𝙤𝙤𝙭 🎧˼", reply_markup=InlineKeyboardMarkup(EVAA),)
    os.remove(f"blackpink_{message.from_user.id}.png")
  
