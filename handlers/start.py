import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAPLYqsvOXrTAjFEQ_JYoxVQO2LPkDMAAgkGAAKyxVhVulwgGjIafHUkBA")
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/a69e4648b1e8b334ab8ab.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 ʜᴇʏ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}),  ɪ ᴀᴍ ᴀ ᴍᴜsɪᴄ ʙᴏᴛ, ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ....

ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ʜᴀɴᴅʟᴇʀs : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★
┣★ ᴍᴀᴅᴇ ʙʏ: [❛-𝐌𝐑'𝐁𝐀𝐍𝐍𝐀-𝐱𝐃°](t.me/MR_ROCKEY_BOY)
┣★
┗━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ_xᴅ](t.me/BANNA_XD) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ​ 🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "❣️ ᴏᴡɴᴇʀ ❣️", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "💥 sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/Wajahtumho"
                    )
                ],[
                    InlineKeyboardButton(
                        "🌹ᴄʜᴀɴɴᴇʟ🌹", url="https://t.me/Couple_vibz"
                    ),
                    InlineKeyboardButton(
                        "😎 ᴅᴇᴠᴇʟᴏᴘᴇʀ 😎", url="https://t.me/BANNA_XD"
                    )]
            ]
       ),
    )

