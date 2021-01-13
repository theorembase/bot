import logging
import whois
# import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    w = whois.whois(update.message.text)
    print("\n")
    print(w.name_servers)
    print(w.registrar)
    print(w.status)
    print(w.creation_date)
    print(w.expiration_date)
    print(w.emails)
    print(w.name)
    print(w.org)
    print(w.address)
    print(w.city)
    print(w.state)
    print(w.zipcode)
    print(w.country)
    m = ["Domain Name:",w.domain_name,"Registrar:",w.registrar,"status:",w.status,"","","Name:",w.name,"Emails:"," , ".join(w.emails)]
    print(m)
    update.message.reply_text("\n".join(m))#,"Registrar: ",w.registrar,"\n")
    # except:
    #     update.message.reply_text("Error Occured Try 1 - 3 times more")#,"Registrar: ",w.registrar,"\n")
    # update.message.reply_text(w.domain_name)



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1487976162:AAEkFoFiX2Rp4LK_JpVGczro9AZbhClrFnw", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=43,
                          url_path="1487976162:AAEkFoFiX2Rp4LK_JpVGczro9AZbhClrFnw")
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook("EARNEY" + "1487976162:AAEkFoFiX2Rp4LK_JpVGczro9AZbhClrFnw")

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
