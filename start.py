import requests
import telebot
from telebot import types
from gatet import Tele 
token = '7383314239:AAHFal_jdJ9PAIsx9GxkYSVrkeaVdDwuPyQ'
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 𝗖𝗼𝗺𝗯𝗼 𝗙𝗶𝗹𝗲")
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.reply_to(message, "Stopping the bot...")
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
				cm4 = types.InlineKeyboardButton(f"• ❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱  : [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 📊 𝗧𝗼𝘁𝗮𝗹 : [ {total} ] •", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm5)
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
