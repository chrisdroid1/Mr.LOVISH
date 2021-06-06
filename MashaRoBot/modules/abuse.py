import random

import os 

import asyncio

from telethon import events

from MashaRoBot import pbot

REPLY_STRING = (

        "Jaa na Bsdk, gaand mara jaake.",

    "Tu paidaishi chutiya hai ki koi course kiya hai? ",

    "I came to know that some shops were selling your ass for 69$",

    "The world would have been so smooth if your dad had just pulled out",

    "And the truth is, you're a fucking cunt",

    "What else can you do other than spreading your legs?",

    "Jaa na Gandu",

    "Aand ka na Gaand ka, Gyaan jhaare pure Brahmand ka",

    "Dhaat teri maa ki ch*t",

    "Gaand se tatti nikalke jaadugar samajhta hai apne aap ko?",

    "Bitches be trippin'",

    "Please fuck off bitch, and get a life",

    "Tu aise nhi maanega - Mat maan, maa chuda",

    "Tujhse zada sundar teri jali hui gaand hai",

    "Ye aapki Randikhana nhi hai, kripya yaha se dur rahe",

    "I'm a good girl, I don't abuse. But you're a bitch.",

    "RANDI CHOD KE MUTH MAAR SALE",

    "TERI MAA KI CH*T...💦me khira",

    "ANDi mandi RANDI TERI GF HAI EAK no. ki randi🙂",

    "oye bosari chod ke lodi deen ke",

    "mu me le lodu",

    "gand me lega ya mu me mere lund?",

    "oyee hoyee🤤🤤Teri gori gori ch*tchusne de🤤💦",

    "oye behencooo apni behen ko chod ka ke😡",

    "ladwa le le mere😆",

    "pani kaam hai matke me maar lunga teri eak jatke me😆",

    "gaye ke piche pada hai sand tere jaise mere niche latak rehe hai 2 aand😆😆",

)

@pbot(cmd="/abuse (/*)")

async def abuse(event): 

        await pbot.reply_text(random.choice(REPLY_STRING))

        await get_start_func(message)
