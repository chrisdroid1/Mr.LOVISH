import random

from telegram.ext import run_async, Filters

from telegram import Message, Chat, Update, Bot, MessageEntity

from MashaRoBot import dispatcher

from MashaRoBot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (

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

    "bsdkeee jyada na bol rha he",

    "saale gand marwa apni",
  
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

    "gaye ke piche pada hai sand tere jaise mere niche latak rehe hai 2 aand😆😆"

  )

@run_async

def abuse(bot: Bot, update: Update):

    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages

    message = update.effective_message

    if message.reply_to_message:

      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))

    else:

      message.reply_text(random.choice(SFW_STRINGS))

ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)

dispatcher.add_handler(ABUSE_HANDLER)
