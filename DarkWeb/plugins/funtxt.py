import nekos

from Dark.utils import admin_cmd, edit_or_reply, sudo_cmd
from DarkWeb import CMD_HELP
from DarkWeb.cmdhelp import CmdHelp


@Dark.on(admin_cmd(pattern="ftext ?(.*)"))
@Dark.on(sudo_cmd(pattern="ftext ?(.*)", allow_sudo=True))
async def payf(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        paytext = input_str
        pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
            paytext * 8,
            paytext * 8,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 6,
            paytext * 6,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 2,
        )
    else:
        pay = "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯\n"

    await event.edit(pay)


@Dark.on(admin_cmd(pattern="cat$"))
@Dark.on(sudo_cmd(pattern="cat$", allow_sudo=True))
async def hmm(Dark):
    if Dark.fwd_from:
        return
    reactcat = nekos.textcat()
    await edit_or_reply(Dark, reactcat)


@Dark.on(admin_cmd(pattern="why$"))
@Dark.on(sudo_cmd(pattern="why$", allow_sudo=True))
async def hmm(Dark):
    if Dark.fwd_from:
        return
    whyDark = nekos.why()
    await edit_or_reply(Dark, whyDark)


@Dark.on(admin_cmd(pattern="fact$"))
@Dark.on(sudo_cmd(pattern="fact$", allow_sudo=True))
async def hmm(Dark):
    if Dark.fwd_from:
        return
    factDark = nekos.fact()
    await edit_or_reply(Dark, factDark)


CmdHelp("funtxts").add_command(
  'cat', None, 'Sends you some random cat facial text art'
).add_command(
  'why', None, 'Asks some random funny questions'
).add_command(
  'fact', None, 'Sends you some random facts'
).add_command(
  'ftext', '<text>', 'Writes your text in "F" format'
).add()
