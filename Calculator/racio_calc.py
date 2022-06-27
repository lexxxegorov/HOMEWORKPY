from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler


bot = Bot(token='5502824711:AAGgGlIsV_HeFdnDVHyD6R3E7QN5pH7jASQ')
updater = Updater(token='5502824711:AAGgGlIsV_HeFdnDVHyD6R3E7QN5pH7jASQ', use_context=True)
dispatcher = updater.dispatcher
START = 0
BIO = 1 
OPER = 2


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Ввведите первое число")
    
    return START 

def input_data_1(update, context):
    global first_number
    first_number = float(update.message.text)
    print (first_number)
    context.bot.send_message(update.effective_chat.id, "Ввведите второе число")
  
    return BIO

def input_data_2(update, context):
    global second_number
    second_number = float(update.message.text)
    print (second_number)
    context.bot.send_message(update.effective_chat.id, "Ввведите операцию")

    return OPER

def do_it(update, context):
  operation = update.message.text
  result = float()
  if operation in ('+', '-', '*', '/'):
    if operation == '+':
      result = first_number + second_number
      print(f'{result} = {first_number} + {second_number}')
    elif operation == '-':
      result = first_number - second_number
      print(f'{result} = {first_number} + {second_number}')
    elif operation == '*':
      result = first_number * second_number
      print(f'{result} = {first_number} + {second_number}')
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
            print(f'{result} = {first_number} / {second_number}')  
        else:
            print("Деление на ноль!")
            context.bot.send_message(update.effective_chat.id, "Деление на ноль!")


    context.bot.send_message(update.effective_chat.id, f'{result}')
  return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
first_handler = MessageHandler(Filters.text, input_data_1)
second_handler = MessageHandler(Filters.text, input_data_2)
operation_handler = MessageHandler(Filters.text, do_it)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states= {START: [first_handler],
                                              BIO: [second_handler],
                                              OPER: [operation_handler]},
                                    fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()
