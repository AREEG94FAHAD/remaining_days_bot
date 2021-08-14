from datetime import date
from flask import Flask, request
import telebot
import os
from helper import days, months, years, daynumber
from datetime import date

import time


# DATEE = os.environ.get('DATEE')
bot = telebot.TeleBot('API')

details = {}
details['day'] = ''
details['month'] = ''
details['year'] = ''

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    details['day'] = ''
    details['month'] = ''
    details['year'] = ''

    msg = bot.send_message(
        message.chat.id, "Select the year", reply_markup=years())




@bot.callback_query_handler(func=lambda call: call.data in [str(i) for i in range(2021, 2037, 1)])
def callback_query(call):

    details['year'] = call.data

    bot.send_message(call.from_user.id, "Select the month",
                     reply_markup=months())


@bot.callback_query_handler(func=lambda call: call.data in [str(i)+'m' for i in range(1, 13, 1)])
def callback_query(call):

    if details['year'] == '':
        bot.send_message(call.from_user.id, "Select the year",
                         reply_markup=years())
    else:
        details['month'] = call.data

        dayNum = daynumber(int(details['year']), int(
            details['month'].replace('m', '')))

        bot.send_message(call.from_user.id, "Select the day",
                         reply_markup=days(dayNum))
    # else:


@bot.callback_query_handler(func=lambda call: call.data in [str(i) for i in range(1, 32, 1)])
def callback_query(call):

    if details['year'] == '' or details['month'] == '':
        details['year'] = ''
        details['month'] = ''
        bot.send_message(call.from_user.id, "Select the year",
                         reply_markup=years())
    else:
        details['day'] = call.data
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        current_date = d1.split('/')

        f_date = date(int(current_date[0]), int(
            current_date[1]), int(current_date[2]))
        l_date = date(int(details['year']), int(
            details['month'].replace('m', '')), int(details['day']))
        delta = l_date - f_date



        bot.send_message(call.from_user.id,'The remaining days are '+str( delta.days))

        details['year'] = ''
        details['month'] = ''
        details['day'] = ''

        bot.send_message(call.from_user.id,'To use it again send anything')


# @bot.message_handler(func=lambda message: True)
# def message_handler(message):

#     details['day'] = ''
#     details['month'] = ''
#     details['year'] = ''
    
#     try:

#         msg = bot.send_message(
#             message.chat.id, "Select the year", reply_markup=years())

#     except:
#         bot.send_message(
#             message.chat.id, 'Something went wrong try agin later')



# @server.route('/' + DATEE, methods=['POST'])
# def getMessage():
#     json_string = request.get_data().decode('utf-8')
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "!", 200


# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://dateremaining.herokuapp.com/' + DATEE)
#     return "!", 200


# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


bot.polling()

