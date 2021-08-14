from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import string
import random

def daynumber(year,month):
    from calendar import monthrange
    return  monthrange(year, month)[1] 
     

def days(monthDays):
    markup = InlineKeyboardMarkup()
    markup.row_width = 5
    day2 = monthDays - 28
    for i in range(1,28+1,4):
        markup.add(InlineKeyboardButton(i, callback_data=str(i)),InlineKeyboardButton(i+1, callback_data=str(i+1)),InlineKeyboardButton(i+2, callback_data=str(i+2)),InlineKeyboardButton(i+3, callback_data=str(i+3)))
    
    if day2 == 0:
        return markup
    else:
        for i in range(day2):
            markup.add(InlineKeyboardButton(i+28, callback_data=str(i+28)))

    return markup

def months():
    markup = InlineKeyboardMarkup()
    markup.row_width = 4
    for i in range(1,13,3):
        markup.add(InlineKeyboardButton(i, callback_data=str(i)+'m'),InlineKeyboardButton(i+1, callback_data=str(i+1)+'m'),InlineKeyboardButton(i+2, callback_data=str(i+2)+'m'))
    return markup

def years():
    markup = InlineKeyboardMarkup()
    markup.row_width = 5
    
    for i in range(2021,2037,4):
        markup.add(InlineKeyboardButton(i, callback_data=i),InlineKeyboardButton(i+1, callback_data=i+1),InlineKeyboardButton(i+2, callback_data=i+2),InlineKeyboardButton(i+3, callback_data=i+3))
    return markup



def yes_no():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    
    markup.add(InlineKeyboardButton('Yes', callback_data='Yes'),InlineKeyboardButton('No', callback_data='No'))
    return markup