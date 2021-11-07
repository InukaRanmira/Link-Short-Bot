

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


app = Client("bitlybot" ,bot_token = TOKEN ,api_id = API_ID ,api_hash = API_HASH )

@app.on_message(filters.private & filters.command(['start']))
async def start(client,message):
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
    
