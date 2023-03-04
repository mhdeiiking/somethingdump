import telebot
import requests
bot = telebot.TeleBot("5448584711:AAFEK6_dDbhyVGuKeCRM-K0B3SNWw8kmJYQ",num_threads=20,skip_pending=True)
def run_command(uu,command):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://redis.io/',
        'Content-Type': 'application/json',
        'Origin': 'https://redis.io',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = {'commands':[command],'id':uu}

    response = requests.post('https://cli.redis.io/', headers=headers, json=data)
    if response.text:
        info = response.json()
        rep = info['replies'][0]
        if rep['error']:
            value = rep['value']
            return str(value)
        else:
            value = rep['value']
            return str(value)
    else:
        return "Unknown"
@bot.message_handler(commands=['start'])
def start(message):
    x = f"Hello <strong>{message.from_user.first_name}</strong>,\n"
    x+="- Welcome to Redis Command Tester!\n"
    x+="- You can try your Redis command from here!\n"
    x+="- Just send Your redis Command Like: <code>set key value</code> !\n"
    x+="- By: @trakoss ."
    bot.reply_to(message,x,parse_mode='html')
@bot.message_handler(func=lambda m:True)
def rec(message):
    x = run_command(message.from_user.id,message.text)
    z = "Server Response:\n"
    z+=f"<code>{x}</code>"
    bot.reply_to(message,z,parse_mode='html')
bot.infinity_polling()

