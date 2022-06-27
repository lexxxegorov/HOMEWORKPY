
from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler


bot = Bot(token='5502824711:AAGgGlIsV_HeFdnDVHyD6R3E7QN5pH7jASQ')
updater = Updater(token='5502824711:AAGgGlIsV_HeFdnDVHyD6R3E7QN5pH7jASQ', use_context=True)
dispatcher = updater.dispatcher
START = 0



def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите элемент поиска: ")
    
    return START 

def get_fromfile(update, context):
    global search
    search = update.message.text
    with open('BD33.txt', 'r', encoding = 'utf=8') as file:
        for line in file:
            if search in line:
                print (line)
                context.bot.send_message(update.effective_chat.id, line)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
first_handler = MessageHandler(Filters.text, get_fromfile)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states= {START: [first_handler]},
                                    fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()
