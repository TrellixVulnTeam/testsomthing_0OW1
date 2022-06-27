import asyncio
import random

from REBELBOT.utils import admin_cmd

from userbot.cmdhelp import CmdHelp


@borg.on(admin_cmd(pattern=r"carry$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("speaking a line.......")
    await asyncio.sleep(2)
    x = random.randrange(1, 25)
    if x == 1:
        await event.edit("To Kaise Hai AAp Log??**")
    elif x == 10:
        await event.edit(
            "Ek to aap muje benchoo benchoo bolna band kijiye , kya bigaada hai meine apka , aap honge benchoo."
        )
    elif x == 11:
        await event.edit(
            "Ganta bancho, sirf dukandaron ka faiyda hota hai isme , aur benchoo kis chutiye ne valentine’s week bnaya hai, pure saal nukkad mein chai biscuit khake paise bchao aur ek hafte mein aise udaa do jaise baap ki koyle ki factory hoo. Banchoo!! "
        )
    elif x == 12:
        await event.edit(
            " Saat din, Sunday se leke agle sunday tak gifts do….Akhand Chuityapa Banchoo !!"
        )
    elif x == 13:
        await event.edit(
            " Woh kehti hai grow some balls, ab doo ke teen kaise karu bancho."
        )
    elif x == 14:
        await event.edit(
            "“Aaj mei thakne ke mood mei nahi thakane ke mood mei hoon..” ... "
        )
    elif x == 15:
        await event.edit("“Joh bistar pe zabaan dete hain woh aksar badal jate hain”")
    elif x == 16:
        await event.edit(
            "Pichwade mein itni goli maroonga ... ki uske bachche pittal ke paida honge"
        )
    elif x == 17:
        await event.edit(
            "Hamara income high ho na ho ... outcome toh hamara bhi world class hai"
        )
    elif x == 18:
        await event.edit("Bhoot bhoot ... inki maa ki ")
    elif x == 19:
        await event.edit(
            "Log sunenge to kya kahenge ... chutiya aashiqui ke chakkar mein mar gaya, aur laundiya bhi nahi mili"
        )
    elif x == 2:
        await event.edit("Mithai Ki Dukan Pe Leke Jaunga200 Me Bik Jayega ")
    elif x == 20:
        await event.edit("Pehli baar mein sabse zyada mazaa aata hai ")
    elif x == 21:
        await event.edit(
            "Pachaas pachaas kos door jab gaon mein Holi hoti hai ... toh maa kehti hai sooja beti sooja ... varna apni pichkaari lekar Jabbar aa jayega "
        )
    elif x == 22:
        await event.edit(
            "Koi madharchod button dabakar mere liye yeh faisla nahin karega ... ki mujhe kab marna hai"
        )
    elif x == 23:
        await event.edit(
            "Aaj kal pyar na naukrani jaisa ho gaya hai ... aata hai, bell bhajata hai, kaam karta hai aur chala jaata hai"
        )
    elif x == 24:
        await event.edit(
            "Meri mardangi ke bare mein aap gaon ki kisi bhi ladki se pooch sakte ho ... report achchi milegi "
        )
    elif x == 25:
        await event.edit("Written and Created By: @MYSTERIOUS_PLUGINS ! thank you🙏🏻❤")
    elif x == 3:
        await event.edit("Ab Aayega Maza Hmmmmmmm ")
    elif x == 4:
        await event.edit(
            "Agar Ye Banda Cricket Mein Commentary KarnaShuru Kar De.. To Match Ka Kya Hoga"
        )
    elif x == 5:
        await event.edit("Tiktokers Ke Kanome Ek Hi Avaj ,To Kiase He Aap Log ")
    elif x == 6:
        await event.edit(
            "Pathhar Se Mat Maro Mere Diwano Ko,Bum Ka Jamana Hai Udado Salo Ko "
        )
    elif x == 7:
        await event.edit("Duniya madar***d thi, madar***d hai aur madar***d rahegi. ")
    elif x == 8:
        await event.edit("Youthube ")
    elif x == 9:
        await event.edit("Aao yaar apne kaano mein earphone daalo.")


CmdHelp("carryminati").add_command("carry", None, "CarryMinati").add()
