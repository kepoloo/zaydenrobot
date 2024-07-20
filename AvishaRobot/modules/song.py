import os

import requests
import yt_dlp
from pyrogram import filters
from youtube_search import YoutubeSearch

from AvishaRobot import SUPPORT_CHAT, pbot,BOT_NAME



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


@pbot.on_message(filters.command(["song"]))
def song(client, message):

    message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = ""
    for i in message.command[1:]:
        query += " " + str(i)
    print(query)
    m = message.reply("🎶")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "**⬤ sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ ᴏɴ ʏᴏᴜᴛᴜʙᴇ, ᴄʜᴋ ᴀɢᴀɪɴ.**"
        )
        print(str(e))
        return
    m.edit("🎶")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**❖ sᴏɴɢ ᴛɪᴛʟᴇ ➥** {title[:25]}\n\n**● ᴅᴜʀᴀᴛɪᴏɴ ➥** {duration}\n**● ᴠɪᴇᴡs ➥** {views}\n\n**❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹ ˹𝙕𝙖𝙮𝙙𝙚𝙣 ✘ 𝙅𝙤𝙤𝙭 🎧˼**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            performer=BOT_NAME,
            thumb=thumb_name,
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit(
            f"**⬤ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴇʀʀᴏʀ, ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ ➥ [sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ](t.me/{SUPPORT_CHAT})**\n\**❅ ᴇʀʀᴏʀ ➥** {e}"
        )
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


__mod_name__ = "sᴏɴɢ"

__help__ = """

⬤ /song ➥ ᴛᴏ  ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴍᴘ3 sᴏɴɢ.
⬤ /vsong ➥ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ sᴏɴɢ.
"""

                       
