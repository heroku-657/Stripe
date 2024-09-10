import requests
import telebot
from telebot import types
from gatet import Tele 

token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(token, parse_mode="HTML")

# Admin chat ID for approval
ADMIN_CHAT_ID = 5372825497  # Replace with your admin chat ID

# File to store approved user IDs
APPROVED_USERS_FILE = "approved_users.txt"

# Global flag to control the process
stop_processing = False

def load_approved_users():
    try:
        with open(APPROVED_USERS_FILE, 'r') as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def save_approved_user(user_id):
    with open(APPROVED_USERS_FILE, 'a') as f:
        f.write(f"{user_id}\n")

approved_users = load_approved_users()

@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) in approved_users:
        bot.reply_to(message, "𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 𝗖𝗼𝗺𝗯𝗼 𝗙𝗶𝗹𝗲")
    else:
        bot.reply_to(message, "You are not authorized to use this bot. Please contact the admin.")

@bot.message_handler(commands=['approve'])
def handle_approve(message):
    if message.chat.id == ADMIN_CHAT_ID:
        try:
            user_id_to_approve = message.text.split()[1]
            approved_users.add(user_id_to_approve)
            save_approved_user(user_id_to_approve)
            bot.reply_to(message, f"User {user_id_to_approve} has been approved.")
        except IndexError:
            bot.reply_to(message, "Please provide a user ID to approve.")
    else:
        bot.reply_to(message, "You are not authorized to approve users.")

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    global stop_processing
    if str(message.chat.id) in approved_users:
        stop_processing = True
        bot.reply_to(message, "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗦𝘁𝗼𝗽𝗽𝗲𝗱...")
    else:
        bot.reply_to(message, "You are not authorized to use this command.")

@bot.message_handler(commands=['help'])
def help(message):
    if str(message.chat.id) in approved_users:
        bot.reply_to(message, "𝗛𝗼𝘄 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗲 𝗯𝗼𝘁\n𝗙𝗶𝗿𝘀𝘁 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗯𝗼𝘁 𝘃𝗶𝗮 /start 𝗰𝗼𝗺𝗺𝗮𝗻𝗱\n𝗧𝗵𝗲𝗻 𝘂𝗽𝗹𝗼𝗮𝗱 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗯𝗼 𝗳𝗶𝗹𝗲\n𝗙𝗶𝗹𝗲 𝘀𝗵𝗼𝘂𝗹𝗱 𝗯𝗲 𝗮𝘀 .𝘁𝘅𝘁 𝗳𝗶𝗹𝗲\n𝗧𝗼 𝘀𝘁𝗼𝗽 𝘁𝗵𝗲 𝗯𝗼𝘁 𝘂𝘀𝗲 /stop 𝗰𝗼𝗺𝗺𝗮𝗻𝗱\n𝗗𝗼𝗻'𝘁 𝘂𝘀𝗲 𝗴𝗲𝗻 𝗰𝗰 𝘁𝗿𝘆 𝘁𝗼 𝘂𝘀𝗲 𝘀𝗰𝗿𝗮𝗽𝗲𝗱 𝗰𝗰\n𝗙𝗼𝗿 𝗮𝗻𝘆 𝗯𝘂𝗴 𝘆𝗼𝘂 𝗳𝗼𝘂𝗻𝗱 𝘀𝗲𝗻𝗱 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗵𝗲𝗿𝗲 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : @fahimhossen27")
    else:
        bot.reply_to(message, "You are not authorized to use this bot. Please contact the admin.")

@bot.message_handler(content_types=["document"])
def main(message):
    global stop_processing
    if str(message.chat.id) in approved_users:
        stop_processing = False  # Reset the flag at the start of the process
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
                    if stop_processing:
                        bot.reply_to(message, "Process was stopped by user.")
                        break
                    
                    try:
                        data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
                    except:
                        pass

                    # Extract data and handle missing fields
                    bank = data.get('bank', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    emj = data.get('country', {}).get('emoji', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    cn = data.get('country', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    dicr = data.get('scheme', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    typ = data.get('type', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    url = data.get('bank', {}).get('url', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')

                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                    cm2 = types.InlineKeyboardButton(f"• ✅ 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 : [ {ch} ] •", callback_data='x')
                    cm3 = types.InlineKeyboardButton(f"• ✅ 𝗔𝗽𝗿𝗼𝘃𝗲𝗱 : [ {live} ] •", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"• ❌ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 : [ {dd} ] •", callback_data='x')
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
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑼𝑪𝑪𝐸𝑺𝑺
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
    else:
        bot.reply_to(message, "You are not authorized to use this bot. Please contact the admin.")

print("Bot is Running")
bot.polling()
