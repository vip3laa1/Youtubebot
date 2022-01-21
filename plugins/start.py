from pyrogram import Client, Filters, StopPropagation


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    welcomed = f"**🧸 ┇  مرحبا بك : <b>{message.from_user.first_name}</b>\n\nيمكنك تحميل من يوتيوب بأستخدام البوت .\nارسل رابط الاغنية فقـط -- -- -- -- -- -- -- -- -- -- -- -- -- --**"
    await message.reply_text(welcomed)
    raise StopPropagation
