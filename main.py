import telebot
from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import flask
import requests

appname="hanbot127"


token = '1065369028:AAEeSsvfOxbpLea-OzqXL9yAtVFiXih8cCA'
bot = telebot.TeleBot (token)

server = flask.Flask(_name_)
apikey="d2082dd3-a3b5-4514-ad00-659abf24e921"

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {'databaseURL':'https://hankaz-f9cdf.firebaseio.com/'})

current_han = 0

@bot.message_handler(commands=['start'])
def StartHandler (msg) :
    name = msg.from_user.first_name
    bot.send_message(msg.chat.id,'привет!')
    AskHan(msg)

def AskHan(msg):
    
    keyboard = types.ReplyKeyboardMarkup()

    btn1 = types.KeyboardButton("Керей")
    btn2 = types.KeyboardButton("Абылай")
    btn3 = types.KeyboardButton("Кенесары")
    btn4 = types.KeyboardButton("Болат")
    btn5 = types.KeyboardButton("Әз-Жәнібек хан")
    btn6 = types.KeyboardButton("Жанибек")
    btn7 = types.KeyboardButton("Бурундук")
    btn8 = types.KeyboardButton("Касым")
    btn9 = types.KeyboardButton("Мамаш")
    btn10 = types.KeyboardButton("Автор")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)
    keyboard.add(btn6)
    keyboard.add(btn7)
    keyboard.add(btn8)
    keyboard.add(btn9)
    keyboard.add(btn10)


    ans = bot.send_message(msg.chat.id, "Выбери хана, о котором хочешь узнать информацию.", reply_markup = keyboard)
    bot.register_next_step_handler(ans, Answer)

def Answer(msg):
    global current_han
    
    if msg.text == "Керей":
        current_han = 1
        info = db.reference("/1/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/1/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Абылай":
        current_han = 2
        info = db.reference("/2/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/2/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Кенесары":
        current_han = 3
        info = db.reference("/3/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/3/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Болат":
        current_han = 4
        info = db.reference("/4/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/4/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Әз-Жәнібек хан":
        current_han = 5
        info = db.reference("/5/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/5/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Жанибек":
        current_han = 6
        info = db.reference("/6/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/6/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Бурундук":
        current_han = 7
        info = db.reference("/7/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/7/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Касым":
        current_han = 8
        info = db.reference("/8/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/8/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Мамаш":
        current_han = 9
        info = db.reference("/9/инфо").get()
        bot.send_message(msg.chat.id, info)
        pop = db.reference("/9/картинка").get()
        bot.send_message(msg.chat.id,pop)
    if msg.text == "Автор":
        current_han = 10
        info = db.reference("/10/Автор").get()
        bot.send_message(msg.chat.id, info)
        
 
    InfHan(msg)
    

def InfHan(msg):

    keyboard = types.ReplyKeyboardMarkup()
    
    btn1 = types.KeyboardButton("Басқаруы ")
    btn2 = types.KeyboardButton("Биография ")
    btn3 = types.KeyboardButton("Назад")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)

    ans = bot.send_message(msg.chat.id, ",,,", reply_markup = keyboard)
    bot.register_next_step_handler(ans,Information )

def Information(msg):
    
    if msg.text == "Басқаруы":
        info = db.reference("/" + str(current_han)+"/Басқаруы").get()
        bot.send_message(msg.chat.id, info)
        InfHan(msg)
    if msg.text == "Биография":
        info = db.reference("/"+ str(current_han)+"/Биография").get()
        bot.send_message(msg.chat.id, info)
        InfHan(msg)
    if msg.text == "Назад":
        AskHan(msg)




    ##bot.polling()

@server.route('/' + token, methods=['POST'])
def get_message():
     bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
     return "!", 200

@server.route('/', methods=["GET"])
def index():
     bot.remove_webhook()
     bot.set_webhook(url=f"https://{appname}.herokuapp.com/{token}")
     return "Hello from Heroku!", 200
     

if _name_ == "_main_":
     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
