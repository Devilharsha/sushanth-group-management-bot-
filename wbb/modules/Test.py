from wbb import app # This is bot's client
from wbb import app2 # userbot client, import it if module is related to userbot
from pyrogram import filters # pyrogram filters
...
@app.on_message(~filters.edited & filters.command("hi"))
async def some_function(_, message):
    await message.reply_text("hi what's up!!")

# Many useful functions are in, wbb/utils/, wbb, and wbb/core/
