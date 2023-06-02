import requests , telebot
from telebot import types

bot = "6287963945:AAEEYcpvN5k_cwHa8I28O8tS0TCe7AKm9Ps"
bot = telebot.TeleBot(bot)

btn1 = types.InlineKeyboardButton(text='؟', callback_data='check')

@bot.message_handler(commands=["start"])
def start(message):
    
    brok = types.InlineKeyboardMarkup()
    brok.row_width = 2
    brok.add(btn1)
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'''
**
مرحبا بك - [{first_name}](tg://settings)
& في بوت معلومات ip 
فقط اضغط على ؟ و ارسل ip 
وانتظر ...
**''', parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=brok)

@bot.callback_query_handler(func=lambda call: True)
def ip(call):
  bot.send_message(call.message.chat.id,'ارسل الان الـ ip')
  if call.data=='check':
   @bot.message_handler(func=lambda m: True)
   def info(message):
    msg = message.text
    try:
    	url = requests.get(f'https://ipinfo.io/{msg}/geo').json()
    	ip = url['ip']
    	ci = url['city']
    	reg = url['region']
    	co = url['country']
    	l = url['loc']
    	org = url['org']
    	tim = url['timezone']
    	bot.send_message(message.chat.id, f'''
    معلومات  ~ {ip} ⤵️


مدينة : {ci}
منطقة : {reg}
رمز الدولة : {co}
المكان : {l}
السكن : {org}
الوحدة الزمنية : {tim}
  ''')
  
    except:
     bot.send_message(message.chat.id,'تأكد من صحة ip ..')
     
     
     
print('bot run')
bot.infinity_polling()
