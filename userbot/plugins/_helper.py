from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd

from userbot import CMD_LIST
from userbot.Config import Config


@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(allow_sudo=True, pattern="help ?(.*)"))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or REBEL_input == "text":
        results = await event.client.inline_query(tgbotusername, "@REBELBOT_SUPPORT")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await edit_or_reply(event, ["NO_BOT"])

        if input_str in CMD_LIST:
            string = f"Commands found in {input_str}:\n"
            for i in CMD_LIST[input_str]:
                string += f"  {i}"
                string += "\n"
            await event.edit(string)
        else:
            await event.edit(f"{input_str} is not a valid plugin!")
