import uvloop
from pyrogram import Client

from .utils.cache import Cache
from .utils.db import Database
from .utils.logger import Logger
from .utils.misc import Commands
from .utils.misc import URLSafe
from config import Config


class Bot(Client):
    log = Logger
    env = Config
    var = Cache
    cmd = Commands
    url = URLSafe
    mdb = Database  # ini sudah benar, disimpan di atribut class

    def __init__(self):
        name: str = self.env.BOT_ID
        api_id: int = self.env.API_ID
        api_hash: str = self.env.API_HASH
        bot_token: str = self.env.BOT_TOKEN

        # Koneksi MongoDB disimpan manual, tidak dikirim ke super
        self.mongodb = dict(
            connection=self.mdb.Client,
            remove_peers=True,
        )

        super().__init__(
            name,
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token,
            plugins=dict(root="plugins")  # kalau kamu pakai plugins
        )

    async def start(self):
        uvloop.install()
        await super().start()
        self.log.info(f'{self.me.id} Started')

    async def stop(self, *args):
        await super().stop()
        self.log.warning('Client Stopped')


Bot = Bot()
