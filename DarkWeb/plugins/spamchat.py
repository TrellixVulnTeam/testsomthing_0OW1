import random, re
import asyncio
from Dark.utils import admin_cmd, sudo_cmd, edit_or_reply
from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.Config import Config

LOGGER = Config.DARKWEB_ID
SUDO_WALA = Config.SUDO_USERS


@Dark.on(admin_cmd(pattern="spmsg (.*)"))
@Dark.on(sudo_cmd(pattern="spmsg (.*)", allow_sudo=True))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    await event.edit(f"{name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name}{name}\n{name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name} {name}\n{name} {name}{name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name}{name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name}{name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name}{name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name}{name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}")
    


CmdHelp("spamchat").add_command(
"spmsg", "<name>", "name type long"
).add()