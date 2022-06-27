from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)
from telethon.utils import pack_bot_file_id

from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="get_admins ?(.*)"))
@bot.on(sudo_cmd(pattern="get_admins ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**⚜️ Admins in this Group ⚜️**: \n"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if input_str:
        mentions_heading = f"Admins in {input_str} Group: \n"
        mentions = mentions_heading
        try:
            chat = await event.client.get_entity(input_str)
        except Exception as e:
            await edit_or_reply(event, str(e))
            return None
    else:
        chat = to_write_chat
        if not event.is_group:
            await edit_or_reply(event, "I dont think this is a group🚶")
            return
    try:
        async for x in event.client.iter_participants(
            chat, filter=ChannelParticipantsAdmins
        ):
            if not x.deleted and isinstance(x.participant, ChannelParticipantCreator):
                mentions += f"\n 🔰 [{x.first_name}](tg://user?id={x.id}) `{x.id}`"
        mentions += "\n"
        async for x in event.client.iter_participants(
            chat, filter=ChannelParticipantsAdmins
        ):
            if x.deleted:
                mentions += f"\n `{x.id}`"
            elif isinstance(x.participant, ChannelParticipantAdmin):
                mentions += f"\n 🔸 [{x.first_name}](tg://user?id={x.id}) `{x.id}`"
    except Exception as e:
        mentions += f" {str(e)}" + "\n"
    if reply_message:
        await reply_message.reply(mentions)
    else:
        await event.client.send_message(event.chat_id, mentions)
    await event.delete()


@bot.on(admin_cmd(pattern="get_bot ?(.*)"))
@bot.on(sudo_cmd(pattern="get_bot ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bots in this Group**: \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = f"Bots in {input_str} group: \n"
        try:
            chat = await borg.get_entity(input_str)
        except Exception as e:
            await event.edit(str(e))
            return None
    try:
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsBots):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += f"\n ⚜️ [{x.first_name}](tg://user?id={x.id}) `{x.id}`"
            else:
                mentions += f"\n [{x.first_name}](tg://user?id={x.id}) `{x.id}`"
    except Exception as e:
        mentions += f" {str(e)}" + "\n"
    await event.edit(mentions)


@bot.on(admin_cmd(pattern="get_id"))
@bot.on(sudo_cmd(pattern="get_id", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit(
                f"🔸 **Current Chat ID:** `{str(event.chat_id)}`\n\n🔰 **From User ID:** `{str(r_msg.sender_id)}`\n\n🤖 **Bot API File ID:** `{bot_api_file_id}`"
            )

        else:
            await event.edit(
                f"🔸 **Current Chat ID:** `{str(event.chat_id)}`\n\n🔰 **From User ID:** `{str(r_msg.sender_id)}`"
            )

    else:
        await event.edit(f"🔸 **Current Chat ID:** `{str(event.chat_id)}`")


CmdHelp("get_them").add_command(
    "get_admins", None, "Gets the list of admins in current chat along with the crator"
).add_command("get_id", "<reply>", "Gets the user id of the replied user.").add_command(
    "get_bot", None, "Gets the list of all the bots in the chat."
).add_command(
    "info", "<reply / username>", "Fetches the information of the user"
).add()
