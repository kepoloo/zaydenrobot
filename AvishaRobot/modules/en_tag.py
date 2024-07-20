from AvishaRobot import pbot as app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **※ ɪ ʟᴏᴠᴇ ʏᴏᴜ...ᰔᩚ**",
           " **※ ғᴏʀɢᴇᴛ ᴍᴇ..ᰔᩚ",
           " **※ ɪ ᴅᴏɴ'ᴛ ʟᴏᴠᴇ ʏᴏᴜ...ᰔᩚ**",
           " **※ ᴍᴀᴋᴇ ɪᴛ ʏᴏᴜʀs ᴘɪʏᴀ, ᴍᴀᴋᴇ ɪᴛ ʏᴏᴜʀs...ᰔᩚ**",
           " **※ ᴊᴏɪɴ ᴍʏ ɢʀᴏᴜᴘ ᴀʟsᴏ...ᰔᩚ**",
           " **※ ɪ ᴋᴇᴘᴛ ʏᴏᴜʀ ɴᴀᴍᴇ ɪɴ ᴍʏ ʜᴇᴀʀᴛ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴀʀᴇ ᴀʟʟ ʏᴏᴜʀ ғʀɪᴇɴᴅs...ᰔᩚ**",
           " **※ ɪɴ ᴡʜᴏsᴇ ᴍᴇᴍᴏʀʏ ᴀʀᴇ ʏᴏᴜ ʟᴏsᴛ ᴍʏ ʟᴏᴠᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛs ʏᴏᴜʀ ᴘʀᴏғᴇssɪᴏɴ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴅɪᴅ ʏᴏᴜ ʟɪᴠᴇ...ᰔᩚ**",
           " **※ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʙᴀʙʏ...ᰔᩚ**",
           " **※ ɢᴏᴏᴅ ɴɪɢʜᴛ, ɪᴛ's ᴠᴇʀʏ ʟᴀᴛᴇ...ᰔᩚ**",
           " **※ ɪ ғᴇᴇʟ ᴠᴇʀʏ sᴀᴅ ᴛᴏᴅᴀʏ...ᰔᩚ**",
           " **※ ᴛᴀʟᴋ ᴛᴏ ᴍᴇ ᴛᴏᴏ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ's ғᴏʀ ᴅɪɴɴᴇʀ ᴛᴏᴅᴀʏ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ's ɢᴏɪɴɢ ᴏɴ...ᰔᩚ**",
           " **※ ᴡʜʏ ᴅᴏɴ'ᴛ ʏᴏᴜ ᴍᴇssᴀɢᴇ...ᰔᩚ**",
           " **※ ɪ ᴀᴍ ɪɴɴᴏᴄᴇɴᴛ...ᰔᩚ**",
           " **※ ɪᴛ ᴡᴀs ғᴜɴ ʏᴇsᴛᴇʀᴅᴀʏ, ᴡᴀsɴ'ᴛ ɪᴛ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴡᴇʀᴇ ʏᴏᴜ ʙᴜsʏ ʏᴇsᴛᴇʀᴅᴀʏ...ᰔᩚ**",
           " **※ ʏᴏᴜ ʀᴇᴍᴀɪɴ sᴏ ᴄᴀʟᴍ ғʀɪᴇɴᴅ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sɪɴɢ, sɪɴɢ...ᰔᩚ**",
           " **※ ᴡɪʟʟ ʏᴏᴜ ᴄᴏᴍᴇ ғᴏʀ ᴀ ᴡᴀʟᴋ ᴡɪᴛʜ ᴍᴇ...ᰔᩚ**",
           " **※ ᴀʟᴡᴀʏs ʙᴇ ʜᴀᴘᴘʏ ғʀɪᴇɴᴅ...ᰔᩚ**",
           " **※ ᴄᴀɴ ᴡᴇ ʙᴇ ғʀɪᴇɴᴅs...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ᴍᴀʀʀɪᴇᴅ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ʜᴀᴠᴇ ʏᴏᴜ ʙᴇᴇɴ ʙᴜsʏ ғᴏʀ sᴏ ᴍᴀɴʏ ᴅᴀʏs...ᰔᩚ**",
           " **※ ʟɪɴᴋ ɪs ɪɴ ʙɪᴏ, ᴛᴏ ᴊᴏɪɴ ɴᴏᴡ...ᰔᩚ**",
           " **※ ʜᴀᴅ ғᴜɴ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴇᴠᴇʀ ʀᴇᴍᴇᴍʙᴇʀ ᴍᴇ...ᰔᩚ**",
           " **※ ʟᴇᴛ's ᴘᴀʀᴛʏ...ᰔᩚ**",
           " **※ ʜᴏᴡ ᴄᴏᴍᴇ ᴛᴏᴅᴀʏ...ᰔᩚ**",
           " **※ ʟɪsᴛᴇɴ ᴍᴇ...ᰔᩚ**",
           " **※ ʜᴏᴡ ᴡᴀs ʏᴏᴜʀ ᴅᴀʏ...ᰔᩚ**",
           " **※ ᴅɪᴅ ʏᴏᴜ sᴇᴇ...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ᴛʜᴇ ᴀᴅᴍɪɴ ʜᴇʀᴇ...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ɪɴ ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ...ᰔᩚ**",
           " **※ ᴀɴᴅ ʜᴏᴡ ɪs ᴛʜᴇ ᴘʀɪsᴏɴᴇʀ...ᰔᩚ**",
           " **※ sᴀᴡ ʏᴏᴜ ʏᴇsᴛᴇʀᴅᴀʏ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜ ғʀᴏᴍ...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ᴏɴʟɪɴᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ᴇᴀᴛ...ᰔᩚ**",
           " **※ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ɪ ᴡɪʟʟ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴀɴᴅ ᴛᴀɢ ᴇᴠᴇʀʏᴏɴᴇ...ᰔᩚ**",
           " **※ ᴡɪʟʟ ʏᴏᴜ ᴘʟᴀʏ ᴛʀᴜᴛʜ ᴀɴᴅ ᴅᴀʀᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛs ʜᴀᴘᴘᴇɴᴇᴅ ᴛᴏ ʏᴏᴜ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴡᴀɴɴᴀ ᴇᴀᴛ ᴄʜᴏᴄᴏʟᴀᴛᴇ...ᰔᩚ**",
           " **※ ʜᴇʟʟᴏ ʙᴀʙʏ...ᰔᩚ**",
           " **※ ᴅᴏ ᴄʜᴀᴛᴛɪɴɢ ᴡɪᴛʜ ᴍᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ sᴀʏ...ᰔᩚ**",
           " **※ ɢɪᴠᴇ ᴍᴇ ʏᴏᴜʀ ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ ᴘʟᴇᴀsᴇ...ᰔᩚ**"
           ]

VC_TAG = [ " ** lupakan aku...💥**",
           " ** aku tidak mencintaimu...💥**",
           " ** Jadikan itu milikmu...💥**",
           " ** Bergabunglah juga dengan grup saya…💥**”,
           " ** Aku menyimpan namamu di hatiku...💥**",
           " ** Dimana semua temanmu...💥**",
           " ** Dalam ingatan siapa kamu kehilangan cintaku...💥**",
           " ** Apa pekerjaanmu...💥**",
           " ** Dimana kamu tinggal...💥**",
           " ** Selamat Pagi sayang...💥**",
           " ** Selamat malam, sudah terlambat...💥**",
           " ** Aku merasa sangat tidak enak hari ini...💥**",
           " ** bicara padaku juga...💥**",
           " ** Makan malam apa malam ini...💥**",
           " ** Apa yang terjadi...💥**",
           " ** kenapa kamu tidak pesan...💥**",
           " ** Saya tidak bersalah...💥**",
           " ** Kemarin seru ya...💥**",
           " ** Kesibukanmu kemarin...💥**",
           " ** Tentang apa kamu...💥**",
           " ** Kamu tetap tenang kawan...💥**",
           " ** Tahukah kamu cara menyanyi, menyanyi...💥**",
           " ** Maukah kamu datang mengunjungiku...💥**",
           " ** berbahagialah selalu kawan...💥**",
           " ** Bisakah kita berteman...💥**",
           " ** Apakah kamu sudah menikah...💥**",
           " ** Dari mana saja kamu begitu sibuk...💥**",
           " ** link ada di bio, gabung sekarang...💥**",
           " ** hanya bercanda...💥**",
           " ** Tahukah anda pemilik grup ini...💥**",
           " ** Pernahkah kamu mengingatku...💥**",
           " ** ayo berpesta...💥**",
           " ** Bagaimana kamu datang hari ini...💥**",
           " ** Bagaimana harimu...💥**",
           " ** Pernahkah kamu melihat...💥**",
           " ** Apakah anda admin disini...💥**",
           " ** Kita bisa berteman...💥**",
           " ** Tentang apa kamu...💥**",
           " ** Dan bagaimana kabar tahanannya...💥**",
           " ** Melihatmu kemarin...💥**",
           " ** Dari mana asalmu...💥**",
           " ** Apakah kamu online...💥**",
           " ** Apakah kamu temanku....💥**",
           " ** Kamu suka makan apa...💥**",
           " ** Tambahkan saya ke grup Anda, saya akan memutar musik dan menandai semua orang....💥**",
           " ** Aku sedih hari ini...💥**",
           " ** Maukah kamu memainkan kebenaran dan tantangan...💥**",
           " ** Apa yang perlu dikhawatirkan jika kamu mempunyai teman sepertimu...💥**",
           " ** apa yang terjadi padamu...💥**",
           " ** kamu mau makan coklat....💥**",
           " ** Halo sayang...💥**",
           " ** Ngobrol dengan saya...💥**",
           " ** Bagaimana menurutmu...💥**"
         ]


@app.on_message(filters.command(["entag", "englishtag" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("⬤ /entag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("⬤ /entag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("⬤ /entag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("⬤ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["bntag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("⬤ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["enstop", "bnstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("⬤ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("ᴛᴀɢ sᴛᴏᴘᴘᴇᴅ....")

