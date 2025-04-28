import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    startmsg = (
        'The bot is up and running. These bots '
        'can store messages in custom chats, '
        'and users access them through the bot.'
    )
    forcemsg = (
        'To view messages shared by bots. '
        'Join first, then press the Try Again button.'
    )

    API_ID = int(os.environ.get('API_ID', 27418440))
    API_HASH = os.environ.get('API_HASH', '0a08a360e0e9f41b9896f655c300d09d')
    OWNER_ID = int(os.environ.get('OWNER_ID', 1927018403))
    MONGO_URL = os.environ.get('MONGO_URL', 'mongodb+srv://wtfbruh:KontolXD#123@fsub.brzgete.mongodb.net/?retryWrites=true&w=majority&appName=fsub')

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '7806291126:AAE3ftBeO61zH3XrHaJ1IFvkQEyXGKJtD9Y')
    DATABASE_ID = int(os.environ.get('DATABASE_ID', '-1002547370737'))

    BOT_ID = BOT_TOKEN.split(':', 1)[0]


Config = Config()
