from pyrogram import filters

from AvishaRobot import pbot
from AvishaRobot.utils.errors import capture_err
from AvishaRobot.utils.functions import make_carbon

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/ZaydenStreamBot?startgroup=true"),
    ],
]

@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            txt = message.reply_to_message.text
        else:
            return await message.reply_text("⬤ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
    else:
        try:
            txt = message.text.split(None, 1)[1]
        except IndexError:
            return await message.reply_text("⬤ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
    m = await message.reply_text("⚡")
    carbon = await make_carbon(txt)
    await m.edit_text("⬤ ᴜᴩʟᴏᴀᴅɪɴɢ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀʙᴏɴ...")
    await pbot.send_photo(
        message.chat.id,
        photo=carbon,
        caption=f"❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹𝙕𝙖𝙮𝙙𝙚𝙣 ✘ 𝙅𝙤𝙤𝙭 🎧˼", reply_markup=InlineKeyboardMarkup(EVAA),
    )
    await m.delete()
    carbon.close()

####
