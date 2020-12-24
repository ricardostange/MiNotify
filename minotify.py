from telegram.ext import Updater, CommandHandler
import threading
import time


# USE YOUR TELEGRAM BOT TOKEN HERE
TOKEN = "YOUR_TOKEN_HERE"
#################################


class MiNotify:

    def __init__(self, token):
        updater = Updater(token=TOKEN)
        dispatcher = updater.dispatcher

        start_handler = CommandHandler('start', self.start)
        dispatcher.add_handler(start_handler)
        updater.start_polling()

        self.started = threading.Event()


    def start(self, update, context):
        self.context = context
        self.update = update
        self.started.set()


    def message(self, text):
        if not self.started.is_set():
            self.wait_for_start()
        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=text)


    def wait_for_start(self):
        self.started.wait()



def main():

    bot = MiNotify(TOKEN)
    bot.wait_for_start()
    bot.message("Bot has started! Lock phone for notification test")
    bot.message("Make sure you have Telegram notifications active on Mi Fit app")
    time.sleep(10) # Notification after 10 seconds
    bot.message("This is a notification test from your bot")



if __name__ == '__main__':
    main()
