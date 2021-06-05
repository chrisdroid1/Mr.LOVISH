from . import *

from pyrogram import *

from pyrogram.types import *

@Client.on_message(filters.new_chat_members)

async def welcome(client, message):

    try:

        btns=InlineKeyboardMarkup(

              [[

              InlineKeyboardButton(text="Channel📡", url="https://t.me/Psycho_Bots")

              ]]

          )

        joiner = await Client.get_me() 

        for user in message.new_chat_members:

            if int(joiner.id) == int(user.id):

                await message.reply_text("Thanks for adding me to your Group :) \nPromote me now to start vc", reply_markup=buttons)

    except Exception as e:

        await Client.send_message(int("1258905497"), f"Chat ID: `{message.chat.id}` \nError while Sending Thanks Message: {e}")

