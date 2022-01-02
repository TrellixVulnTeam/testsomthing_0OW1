import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import REBELversion, bot, LOGS
from userbot.utils import load_module, start_assistant
from var import Var
from userbot.Config import Config

os.system("pip install -U telethon")

LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)
REBEL_PIC = "https://telegra.ph/file/7661ea6e9c4040ca0ba04.jpg"

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("🔰ՏTᗩᖇT ᖇᗴᗷᗴᒪᗷOT🔰")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("⚡ᖇᗴᗷᗴᒪᗷOT ՏTᗩᖇTᑌᑭ ᑕOᗰᑭᒪᗴTᗴᗪ⚡")
    else:
        bot.start()


import glob

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))



if LOAD_ASSISTANT == True:
    path = "userbot/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)
else:
    print("Assitant is Not Loading As U Have Disabled")



print(f"""Hello sir i am REBELBOT!! REBELBOT VERSION :- {REBELversion} YOUR REBELBOT IS READY! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @REBELBOT_SUPPORT ."""
)

import userbot._core

async def REBEL_is_on():
    try:
        if Config.REBELBOT_ID != 0:
            await bot.send_file(
                Config.REBELBOT_ID,
                REBEL_PIC,
                caption=f"༆ʟɛɢɛռɖaʀʏ ᴀғ ʀᴇʙᴇʟʙᴏᴛ༆\n\n**ᴠᴇʀsɪᴏɴ ➪ {REBELversion}**\n\n𝐓𝐲𝐩𝐞 `.ping` or `.alive` ᴛᴏ ᴄʜᴇᴄᴋ! \n\n ᴊᴏɪɴ [ʀᴇʙᴇʟʙᴏᴛ ᴄʜᴀᴛɪɴɢ](t.me/REBEL_BOT_CHATING) ᴛᴏ ǫᴜᴇʀʏ & ᴊᴏɪɴ [ʀᴇʙᴇʟʙᴏᴛ ᴜᴘᴅᴀᴛᴇ](t.me/REBELBOT_SUPPORT) ᴛᴏ ᴋɴᴏᴡ ʀᴇɢʀᴀᴅɪɴɢ ᴜᴘᴅᴀᴛᴇ ᴀɴᴅ ᴀʙᴏᴜᴛ ʀᴇʙᴇʟʙᴏᴛ",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(REBEL_is_on())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
