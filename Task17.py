"""
1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

"""

text  = ' ЯАбВ помню чуабдное мгновенввье: Пераедо мной явиаблась вты,'

def new_text(n_text):
    lower_text =  n_text.lower()
    new_text = lower_text.translate({ord(i): None for i in 'а''б''в'})
    return (new_text)

final_text = new_text(text)
print (final_text)