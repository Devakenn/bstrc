import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "9025253"))
API_HASH = getenv("API_HASH", "2e8e42d6caffa7806315a085df701e10")
BOT_TOKEN = getenv("BOT_TOKEN", "5662611372:AAH6dZuk4gmcz3lUaU51LXWOBwiEUetyxb8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "1BJWap1sBu8HWP-Ef7YJTBTQcHMLZKT0Yj34y8-03SSV9t9uy9M_wlnSqBeQGj2-G5K5M6fP1ywqsztPY4GNYeZV7rH2gwQC90vnaRRNk1qZwS_ICKXV_15knNdMHmaD90B-d8rKMv36aSuQiIcYnxXmlw36FueoL3RP795alD8HrIfgNu_EqwSDNo8-fewxjd0ef1_ZiXgb5DkrntmdFHLpPZ-0QYjSwVDH5Y4vprQ-VWLhS3sc5lANzgqz-n-8h8MrfDFQDl24R7GroGIBGs3YY9WRp9WExceI-EHsq4p9VXTYOvyPXpAgrvdvTEayRWPzMHbJsC5wrlwvp3MTWurrHhNBLsPo=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
