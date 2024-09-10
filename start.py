import requests
import telebot
from telebot import types
from gatet import Tele 
token = '7383314239:AAHFal_jdJ9PAIsx9GxkYSVrkeaVdDwuPyQ'
bot=telebot.TeleBot(token,parse_mode="HTML")
suu = '/stop'
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 𝗖𝗼𝗺𝗯𝗼 𝗙𝗶𝗹𝗲")
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.reply_to(message, "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗦𝘁𝗼𝗽𝗽𝗲𝗱...")
    bot.stop_polling()
@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, "𝗛𝗼𝘄 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗲 𝗯𝗼𝘁\n𝗙𝗶𝗿𝘀𝘁 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗯𝗼𝘁 𝘃𝗶𝗮 /start 𝗰𝗼𝗺𝗺𝗮𝗻𝗱\n𝗧𝗵𝗲𝗻 𝘂𝗽𝗹𝗼𝗮𝗱 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲\n𝗙𝗶𝗹𝗲 𝘀𝗵𝗼𝘂𝗹𝗱 𝗯𝗲 𝗮𝘀 .𝘁𝘅𝘁 𝗳𝗶𝗹𝗲\n𝗧𝗼 𝘀𝘁𝗼𝗽 𝘁𝗵𝗲 𝗯𝗼𝘁 𝘂𝘀𝗲 /stop 𝗰𝗼𝗺𝗺𝗮𝗻𝗱\n𝗗𝗼𝗻'𝘁 𝘂𝘀𝗲 𝗴𝗲𝗻 𝗰𝗰 𝘁𝗿𝘆 𝘁𝗼 𝘂𝘀𝗲 𝘀𝗰𝗿𝗮𝗽𝗲𝗱 𝗰𝗰\n𝗙𝗼𝗿 𝗮𝗻𝘆 𝗯𝘂𝗴 𝘆𝗼𝘂 𝗳𝗼𝘂𝗻𝗱 𝘀𝗲𝗻𝗱 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗵𝗲𝗿𝗲 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : @fahimhossen27")
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def handlet_stop(call):
    bot.stop_polling()
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗮𝗿𝗱𝘀...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"• ✅ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 : [ {ch} ] •", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"• ✅ 𝗔𝗽𝗿𝗼𝘃𝗲𝗱 : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• ❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 : [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 📊 𝗧𝗼𝘁𝗮𝗹 : [ {total} ] •", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"• 𝗦𝘁𝗼𝗽 •", call.data='stop')
				
				mes.add(cm1, cm2, cm3, cm4, cm5, cm6)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f'''𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗙𝗶𝗹𝗲.... 🗃️''', reply_markup=mes)
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "Your card was declined."
				
				msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ #Approved
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 1$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @fahimhossen27
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				print(last)
				if "cvc" in last:
					bot.reply_to(message, msg)
					live += 1
				elif "funds" in last:
					live += 1
					bot.reply_to(message, msg)
				elif "live" in last:
					ch += 1
					msg1 = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑈𝑪𝑪𝐸𝑆𝑆
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 1$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @fahimhossen27
◆ 𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg)
				else:
					dd += 1
	except:
		pass
print("Bot is Running")
bot.polling()
