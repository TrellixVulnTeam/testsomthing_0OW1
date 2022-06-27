import requests
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd

from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="ytube (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ytube (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://www.youtube.com/results?search_query={input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **UThoob** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="ddg (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ddg (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://duckduckgo.com/?q={input_str.replace(" ", "+")}&t=h_&ia=about'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **duckduckgo** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="altn (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="altn (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://www.altnews.in/?s={input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **altnews** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="var (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="var (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://dashboard.heroku.com/apps/{input_str.replace(" ", "+")}/settings'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **var** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="lmlog (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lmlog (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://dashboard.heroku.com/apps/{input_str.replace(" ", "+")}/logs'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **log** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="hacc (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="hacc (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://dashboard.heroku.com/account/{input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **Heroku Account** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="lmkp (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lmkp (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://indiankanoon.org/search/?formInput={input_str.replace(" ", "+")}+sortby%3Amostrecent'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **Indiankanoon.com : Place** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="gem (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gem (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://mkp.gem.gov.in/search?q={input_str.replace(" ", "+")}&sort_type=created_at_desc&_xhr=1'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me **gem.gov.in** that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="rchiv (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rchiv (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://web.archive.org/web/*/{input_str.replace(" ", "+")}'

    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event,
            f"Let me run your link on wayback machine that for you:\n👉 [{input_str}]({response_api.rstrip()})\n`Thank me later 😉` ",
        )

    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


CmdHelp("search").add_command(
    "rchiv", "<query>", "Gives you the archive link of given query from WayBack Machine"
).add_command(
    "gem",
    "<query>",
    "Gives you the link of given query from Government e-Marketplace (gem.gov.in)",
).add_command(
    "lmkp", "<query>", "Gives you the link of given query from Indiankanoon.org"
).add_command(
    "hacc", None, "Redirects you to your heroku account"
).add_command(
    "lmlog", None, "Redirects you to your app's log page"
).add_command(
    "var", None, "Redirects you to your app's var section"
).add_command(
    "ytube", "<query>", "Gives you the link of given query from youthube"
).add_command(
    "altn", "<query>", "Gives you the link for given query from Alt News"
).add_command(
    "ddg", "<query>", "Gives you the link for given query from Duckduckgo"
).add()
