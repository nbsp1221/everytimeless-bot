import dotenv
import os

# Uncomment the following line to use `.env`.
# dotenv.load_dotenv(verbose=True)

telegram_bot = {
    'token': os.getenv('TELEGRAM_BOT_TOKEN'),
    'chat_id': os.getenv('TELEGRAM_BOT_CHAT_ID')
}

everytime = {
    'id': os.getenv('EVERYTIME_ID'),
    'password': os.getenv('EVERYTIME_PASSWORD')
}
