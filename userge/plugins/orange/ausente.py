# @Laranjudo - Lindo e maravilhoso #
""" Módulo retrabalhado para o Modo Ausente com escolhas aleatórias"""
import asyncio
import random
from userge import Message, userge

# Motivos 

STATUS = (
    "Posso ter saído ou simplesmente estou assistindo agora.",
    "Não estou, não tá vendo?",
    "Estou em algum lugar, menos aqui.",
    "Não cansa?",
    "Queria mesmo era chocolate, mas chocolate branco. Vai me dar?",
    "AUTO REPLY fofo(a)!",
    "Qual parte do AFK tu não entendeu?",
    "NÃO ESTOU!",
)

# Ações - Media dos Motivos 
STATUSM = (
        "https://telegra.ph/file/2b4e417b73b1be05518c7.gif", #Criar novos layouts
)

@userge.on_cmd(
    "status",
    about={
        "header": "Modo Ausente já definido os status/medias",
        "flags": {
            "-au": "Modo Ausente: Ligado...",
            "-a": "Assistindo...",
            "-d": "Dormindo...",
            "-o": "Ocupado....",
            "-n": "Netflix...",
            "-s": "Spotify...",
            "-w": "Working...",
            "-p": "Working...",
            "-dd": "Disney+...",
        },
        "como usar": "{tr}status -flag",
        "exemplo": "{tr}status-au",
    },
    del_pre=True,
    allow_channels=False,
)

async def escolhas_ausente(message: Message):
    """ Motivos para o Modo Ausente """
    await message.edit("`𝙴𝚗𝚝𝚎𝚗𝚍𝚒, 𝙼𝚎𝚜𝚝𝚛𝚎. 𝙰𝚐𝚞𝚊𝚛𝚍𝚎... 𝙼𝚘𝚍𝚘 𝙰𝚞𝚜𝚎𝚗𝚝𝚎 𝚙𝚛é-𝚍𝚎𝚏𝚒𝚗𝚒𝚍𝚘 𝚊𝚝𝚒𝚟𝚊𝚍𝚘 ✅`", log=__name__)
    if "au" in message.flags:
            await message.edit(
                f"!afk {random.choice(STATUS)} | {random.choice(STATUSM)}",
                del_in=1,
            )
    if "an" in message.flags:
            await message.edit(
                f"!afk {random.choice(ANIMU)} | {random.choice(ANIMUM)}",
                del_in=1,
            )
    if "d" in message.flags:
            await message.edit(
                f"!afk {random.choice(DORMINDO)} | {random.choice(DORMINDOM)}",
                del_in=1,
            )
    if "o" in message.flags:
            await message.edit(
                f"!afk {random.choice(OCUPADO)} | {random.choice(OCUPADOM)}",
                del_in=1
            )
    if "n" in message.flags:
            await message.edit(
                f"!afk {random.choice(NETFLIX)} | {random.choice(NETFLIXM)}",
                del_in=1
            )
    if "s" in message.flags:
            await message.edit(
                f"!afk {random.choice(SPOTIFY)} | {random.choice(SPOTIFYM)}",
                del_in=1
            )
    if "w" in message.flags:
            await message.edit(
                f"!afk {random.choice(WORKING)} | {random.choice(WORKINGM)}",
                del_in=1
            )
    if "p" in message.flags:
            await message.edit(
                f"!afk {random.choice(PURPLE)} | {random.choice(PURP)}",
                del_in=1
            )
    if "dd" in message.flags:
            await message.edit(
                f"!afk {random.choice(DISNEYPLUS)} | {random.choice(DISNEYPLUSM)}",
                del_in=1
            )

@userge.on_cmd(
    "bye",
    about={
        "titulo": "Gone!",
        "como usar": "{tr}bye",
        "exemplo": "{tr}bye",
    },
    del_pre=True,
    allow_channels=False,
)

async def gone(message: Message):
    gif = f"""{random.choice(GIFF)}"""
    mensagem = f"<i>I'v to go, bye!</i> :3"
    await message.client.send_animation(
                         message.chat.id, 
                         animation=gif, 
                         caption=mensagem,
    )  
