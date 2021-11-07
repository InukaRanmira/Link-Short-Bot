from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram import Client, filters
import requests 
import json 
import os

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID",12345))
API_HASH = os.environ.get("API_HASH","")
BITLY_TOKEN = os.environ.get("BITLY_TOKEN","")

headers = {
    'Authorization': BITLY_TOKEN,
    'Content-Type': 'application/json',
}

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again 😊"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel 🗣", url=f"https://t.me/szteambots") 
        ]]      
    )


app = Client("bitlybot" ,bot_token = TOKEN ,api_id = API_ID ,api_hash = API_HASH )

@app.on_message(filters.private & filters.command(['start']))
async def start(client,message):
  try:
      await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
  except UserNotParticipant:
      await message.reply_text(
      text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
  )
      return
  await message.reply_sticker(sticker = "CAACAgUAAxkBAAEDVKxhh6qgng7mU5fdxwZTyIEvi2_d7gAC1AQAAi4FOVSJf_SZU2UV7yIE")
  await message.reply_text(f"Hello {message .from_user.first_name}\nhello i am SZ short link genrator\n made by @InukaRanmira ", reply_to_message_id = message.message_id)
  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("SZ Bots News 🙋‍♀️", url="https://t.me/szteambots")],

           [InlineKeyboardButton("Bot Support 💬", url="https://t.me/slbotzone"),

	       InlineKeyboardButton("Follow", url="https://github.com/InukaRanmira"),

	       InlineKeyboardButton("Developer 👑",url = "https://t.me/InukaRanmira")]])
@app.on_message(filters.private & filters.regex("http|https"))
async def Bitly(client,message):
  URL = message.text
  DOMAIN = "bit.ly"
  value  = {'long_url': URL , 'domain': DOMAIN}
  data = json.dumps(value)
  try:
    r = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers,data = data )
    result = r.json()
    link = result["link"]
    await message.reply_text(f"```{link}```", reply_to_message_id= message.message_id)
  except Exception as e :
    await message.reply_text(e)
    
app.run()
    
