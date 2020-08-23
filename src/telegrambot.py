import telegram
import telegram.ext

class TelegramBot():
    def __init__(self, token, chat_id):
        self._token = token
        self._chat_id = chat_id
        self._bot = telegram.Bot(self._token)
        self._updater = telegram.ext.Updater(self._token, use_context=True)

    def add_command_handler(self, command, callback):
        dp = self._updater.dispatcher
        dp.add_handler(telegram.ext.CommandHandler(command, callback))

    def send_message(self, message):
        self._bot.send_message(self._chat_id, message)

    def start(self):
        self._updater.start_polling()
        self._updater.idle()
