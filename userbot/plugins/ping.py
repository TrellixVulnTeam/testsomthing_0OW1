#PIC ADDED BY MAFIA OWNER

import asyncio
from datetime import datetime
from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from ..cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK WEB"
h1m4n5hu0p = borg.uid
DARK_IMG = Config.ALIVE_PIC


@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "__**(❛ ᑭσɳց ❜!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    if DARK_IMG:
        DARK_caption = f"╰•★★  ℘ơŋɠ ★★•╯\n\n    ⚘  `{ms}`\n    ⚘  Oɯɳҽɾ [{DEFAULTUSER}](tg://user?id={h1m4n5hu0p})"
        await event.client.send_file(
            event.chat_id, DARK_IMG, caption=DARK_caption
        )
        await event.delete()


CmdHelp("ping").add_command(
  "ping", None, "Shows you the ping speed of server"
).add()
