import telebot
import random
from telebot import types

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7163947722:AAEDivZ_-yscYgcboMnRiErB-i9JbOUOZtk')

# Dictionary containing 6 words for prediction
prediction_words = ["BIG", "SMALL", "RED", "GREEN", "BIG + GREEN", "SMALL + GREEN", "BIG + RED", "SMALL + RED"]

# Dictionary to keep track of user states (whether password is entered or not)
user_states = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_states[message.chat.id] = {'password_entered': False}
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    bot.reply_to(message, f"*Welcome {message.from_user.first_name} !\n\n⚠️ To  Start the Bot👿 Please Choose a Plan then Buy the Access Key 🔐.\nEnjoy Your Earnings 😜💸\n\n🔥 Bot Pricing Plans\n\n🔹 1 Day Plan :  ( Price : ₹400)\n\n- Duration : 1 Days\n- 5 Sureshots Per Day ( 100% Winning )\n- Features : Bot Access Key + Exclusive VIP Channel Access\n- Price :  ₹400 Only\n\n🔸  7 Days Plan :  ( Price : ₹2,000)\n\n- Duration : 7 Days\n- 7 Sureshots Per Day(100% Winning)\n- Features : Bot Access Key + Exclusive VIP Channel Access\n- Price : ₹2,000 Only\n\n📌 Note : Prices Vary with Different Plans and Affordability-Specific Features.*", reply_markup=markup, parse_mode='Markdown')
    markup.row_width = 1  # Set the number of buttons per row
    markup.resize_keyboard = True  # Allow keyboard to be resized if needed
    markup.one_time_keyboard = False  # Keep keyboard active after button press
    itembtn1 = types.KeyboardButton('START ▶')
    itembtn2 = types.KeyboardButton('PREDICTION 💹')
    itembtn3 = types.KeyboardButton('USER STATISTICS 👥')
    itembtn4 = types.KeyboardButton('SUPPORT 🧑‍💻')
    itembtn5 = types.KeyboardButton('BUY ACCESS KEY 🔐')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(message.chat.id, "*Choose an Option ⬇️ :*", reply_markup=markup , parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "BUY ACCESS KEY 🔐")
def handle_buy_access_key(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🔹 1 Day Plan", callback_data="pro_plan")
    btn2 = types.InlineKeyboardButton("🔸 7 Days Plan", callback_data="legend_plan")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "*Choose a Plan and Buy Access Key🔐 :*", reply_markup=markup , parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in ["pro_plan", "legend_plan"])
def handle_plan_selection(call):
    chat_id = call.message.chat.id
    if call.data == "pro_plan":
        # Send the first picture
        bot.send_photo(chat_id, photo=open('https://iili.io/JkiHy1j.jpg', 'rb'))
        # Send a message after sending the picture
        bot.send_message(chat_id, "*Thank You for Choosing 1 Day Plan !\n\n After Paid Successfully✅ Take a Screenshot and Send to the Admin @ITZ_OP .*", parse_mode="Markdown")
    elif call.data == "legend_plan":
        # Send the second picture
        bot.send_photo(chat_id, photo=open('https://iili.io/JkiJnEJ.jpg', 'rb'))
        # Send a message after sending the picture
        bot.send_message(chat_id, "*Thank You for Choosing 7 Days Plan !\n\n After Paid Successfully✅ Take a Screenshot and Send to the Admin @ITZ_OP .*", parse_mode="Markdown")





@bot.message_handler(func=lambda message: message.text == "START ▶")
def handle_start(message):
    chat_id = message.chat.id
    if user_states[chat_id]['password_entered']:
        bot.send_message(chat_id, "*You are already\nConnected to the server 🛜 🌐 ✅*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, "*Enter Access Key to Start the Bot ⚠️*", parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "PREDICTION 💹")
def handle_prediction(message):
    chat_id = message.chat.id
    if user_states[chat_id]['password_entered']:
        bot.send_message(chat_id, "*Enter 14 Digits Period Number ⬇️ :*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, "*Please ⚠️ Enter the Access Key 🔐*", parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "USER STATISTICS 👥")
def handle_user_statistics(message):
    bot.send_message(message.chat.id, f"* ⚠️ 𝚁𝚎𝚏𝚛𝚎𝚜𝚑𝚒𝚗𝚐...🔄 *", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"* 🌐 Current Online Users : {random.randint(55, 155)}*", parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "SUPPORT 🧑‍💻")
def handle_support(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Join Channel 💥", url="https://t.me/hacker_god_itzop"))
    bot.send_message(chat_id, "* ☎️  Need Help  ⁉️\n\n ⚠️ HOW TO BECOME A MEMBER OF MY TEAM✅\n\n🔰Joining Link 🔗\nhttps://goagames.in/#/register?invitationCode=23661410046\n\n1.✅ Register in Above Link\n2.✅ Deposit Min. ₹1200 +\n3.✅ SMS Your UID To @ITZ_OP\n4.✅ Get Verified \n5.✅ Congratulations 🎉\nYou are a member of my Team.\n\n📌 If You Want To Buy Access Key 🔐  or Need Any Type Of Help From Me\n⬇️ Contact Me On Below Username ⬇️\n\n⚠️ Contact Admin : @ITZ_OP\n\n💬 Join the Given Channel for All  Proofs and All Update's Of the Bot😈\n\n................STAY UPDATED ✌️................\n\n--------------------- × × × --------------------*", reply_markup=markup , parse_mode="Markdown")

@bot.message_handler(func=lambda message: not user_states[message.chat.id]['password_entered'])
def handle_password(message):
    chat_id = message.chat.id
    if message.text == "FUCKGGBYITZOP1005":  # Replace 'YOUR_PASSWORD_HERE' with your actual password
        user_states[chat_id]['password_entered'] = True
        bot.send_message(chat_id, "*🌐Connected to Server Successfully✅*", parse_mode="Markdown")
        bot.send_message(chat_id, "* ⚠️  WELCOME  ⚠️\n\n ✅ Thanks For Being a VIP Member\n Of Our Team 🔥\n\n💹 Use More..........\n🤑 Earn More..........*", parse_mode="Markdown")

        # Sending message to join VIP channel with button
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Join VIP Channel 🔥", url="https://t.me/+ttT4iP0nBlhiMThl"))
        bot.send_message(chat_id, "*💬 Join Our VIP Channel to Get All Updates Of the Bot😈*", reply_markup=markup , parse_mode="Markdown")
        bot.send_message(chat_id, "*⚠️ Press  [PREDICTION]  Botton For Getting Predictions 🔥*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, "*🚫 Invalid Access Key🔐  ⚠️*", parse_mode="Markdown")

@bot.message_handler(func=lambda message: user_states[message.chat.id]['password_entered'] and message.text.isdigit() and len(message.text) == 14)
def handle_period_number(message):
    chat_id = message.chat.id
    prediction = random.choice(prediction_words)
    bot.send_message(chat_id, f"* ⌛ 𝙻𝚘𝚊𝚍𝚒𝚗𝚐...{random.randint(10, 25)}% *", parse_mode="Markdown")
    bot.send_message(chat_id, f"* ⌛ 𝙻𝚘𝚊𝚍𝚒𝚗𝚐......{random.randint(35, 75)}% *", parse_mode="Markdown")
    bot.send_message(chat_id, f"* ⌛ 𝙻𝚘𝚊𝚍𝚒𝚗𝚐.........{random.randint(80, 95)}% *", parse_mode="Markdown")
    bot.send_message(chat_id, f"* 🚦 GOA GAMES 1 MIN - WINGO 🚦\n\n 🚀 PERIOD : {message.text} 🔥\n\n 💹 PREDICTION : {prediction} 🤑\n\n            🎯 Accuracy : {random.randint(75, 95)}% ✅\n\n ⚠️ ( USE 1% or 2% OF CAPITAL ) ⚠️*", parse_mode="Markdown")

@bot.message_handler(func=lambda message: user_states[message.chat.id]['password_entered'] and not message.text.isdigit() or len(message.text) != 14)
def handle_invalid_period_number(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "*❌ Invalid Period Number ⚠️*", parse_mode="Markdown")
    bot.send_message(chat_id, "*Enter 14 Digits Period Number ⬇️ :*", parse_mode="Markdown")

bot.polling()