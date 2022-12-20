import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "12103782"))
API_HASH = getenv("API_HASH", "c7407238fc27d47705106d6b76253bdc")
BOT_TOKEN = getenv("BOT_TOKEN", "5516806812:AAHr5whouEf65SonwlzincuzF1mJOaUUun8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQCmw2BDARRpCQn5UW9_GE6S9mBcBbpFbJj23wSDVNEWt-bBBDRQdz2JVrwCUya5YWqUqDA6whUN-uDrxEZvL793TMdPAxzROVigzml3kbLEkqWkHdzlPrJzwgsiw8A2lnDbgs_3sQ02p9EJoC2vk1mIwmmHl4qDYvoMLuAxIpitoRS1cw55asLQrtumFEhQzBLsRY2yn4CUEvUBvf8Abu7PmubZ2Do1sJXdI6Ghlpp55718dMBqsiaJ8awb7BxSWFvn_9MKIBfOj9eMoLq8BsawSAhCFhYP3o8awyOtUuKTugSDKhRaZ1UGRF6IGB6RaFqx-LlsuzHGoHdKffZLyIe3AAAAAVT_ZpUA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5186954055").split()))
