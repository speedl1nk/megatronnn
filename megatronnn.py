from telegram.ext import Updater , CommandHandler

def greet_user(bot,update):
    text ='Вызван /start'
    print(text)
    update.message.collect_additional_context(text)


def main():
    mybot = Updater("1694428402:AAGYw7nhMTi81JWh3fA0I9MIKe3NhYBS6kU")
    dp =   mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    
    mybot.start_polling()
    mybot.idle()

main()
