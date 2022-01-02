from telethon import events

from userbot import ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/d5a71ebce68e1568b5a74.jpg"
pm_caption = "➥ **ᗩՏՏIՏTᗩᑎT :** `ONLINE`\n\n"
pm_caption += "➥ **ՏYՏTᗴᗰՏ ՏTᗩTՏ**\n"
pm_caption += "➥ **TᗴᒪᗴTᕼOᑎ ᐯᗴᖇՏIOᑎ:** `1.15.0` \n"
pm_caption += "➥ **ᑭYTᕼOᑎ:** `3.8.6` \n"
pm_caption += "➥ **ᗪᗩTᗩᗷᗩՏᗴ ՏTᗩTᑌՏ:**  `Functional`\n"
pm_caption += "➥ **ᑕᑌᖇᖇᗴᑎT ᗷᖇᗩᑎᑕᕼ** : `master`\n"
pm_caption += f"➥ **ᐯᗴᖇՏIOᑎ** : `2.0`\n"
pm_caption += f"➥ **ᗰY ᗰᗩՏTᗴᖇ** : {DEFAULTUSER} \n"
pm_caption += "➥ **ᕼᗴᖇOKᑌ ᗪᗩTᗩᗷᗩՏᗴ** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **ᒪIᑕᗴᑎՏᗴ** : [GNU General Public License v3.0](github.com/REBEL75/REBELSBOTS/blob/master/LICENSE)\n"
pm_caption += "➥ **ᑕOᑭYᖇIᘜᕼT** :[『𝐑𝐄𝐁𝐄𝐋𝐁𝐎𝐓』](https://t.me/REBELBOT_SUPPORT)\n"
pm_caption += "[『𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐁𝐘 𝐑𝐄𝐁𝐄𝐋𝐁𝐎𝐓』](https://t.me/REBELBOT_SUPPORT)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
