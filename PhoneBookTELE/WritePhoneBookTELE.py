
from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler


bot = Bot(token='5502824711:AAGgGlIsV_HeFdnDVHyD6R3E7QN5pH7jASQ')
updater = Updater(token='5502824711:AAGgGlIsV_HeFdnDVHyD6R3E7QN5pH7jASQ', use_context=True)
dispatcher = updater.dispatcher
START = 0
NAME = 1 
SUR = 2
TEL = 3


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите имя (ввод на латинице): ")
    
    return START 

def input_name (update, context):
    global name
    name = update.message.text
    print (name)
    context.bot.send_message(update.effective_chat.id, "Ввведите фамилию: ")

    return NAME

def input_surname(update, context):
    global surname
    surname = update.message.text
    print (surname)
    context.bot.send_message(update.effective_chat.id, "Ввведите телефон: ")
  
    return SUR

def input_telephon(update, context):
    global tele
    tele = update.message.text
    print (tele)
    context.bot.send_message(update.effective_chat.id, "Ввведите комментарий: ")

    return TEL


def send_to_file(update, context):
    global comment
    comment = update.message.text
    print (comment)  

    with open('BD33.txt', 'r', encoding ='utf-8') as file:
        id = file.readlines()[-1].split(';')[0]

    with open('BD33.txt', 'a', encoding ='utf-8') as file:
        file.write(f'\n{(int (id)) + 1}; {name} {surname};{tele}; {comment}\n')

    context.bot.send_message(update.effective_chat.id, 'Контакт записан!')
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
first_handler = MessageHandler(Filters.text, input_name)
second_handler = MessageHandler(Filters.text, input_surname)
third_handler = MessageHandler(Filters.text, input_telephon)
send_handler = MessageHandler(Filters.text, send_to_file)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states= {START: [first_handler],
                                              NAME: [second_handler],
                                              SUR: [third_handler],
                                              TEL: [send_handler],},
                                    fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()
