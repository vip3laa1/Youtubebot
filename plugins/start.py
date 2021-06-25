from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("الـدعم", url="https://t.me/JMTHON")],
        [InlineKeyboardButton(
            "الـمطور", url="https://t.me/RRRD7")]
    ])
    welcomed = f"ههلا <b>{message.from_user.first_name}</b>\n/help للمـزيد من الـمعلومات"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
