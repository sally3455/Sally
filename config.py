## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAdn8F2YXvWreP_5iI0qxVOjbZvc9aHczvbY7MVn-7KwfwwwA6DK-f1ko0vLr7_c2RY_Mwgc3JbFDKO2YP0JpPvugl4lXA3NvkecCgi8QsX27KeZ6_ReSFws-1nS0dtE02DyDy65mWWm8igLfSZtCflLMuknnf4sJyXedwZY4JOhBcvdY-T1V-803x5uNhhvH8NbTlMhZDFcwZnzynnhwXoxCzJKf05woWnbR0w-6_crxUozHnNpgEnFcp1wDXFw0ax-fxpSkq4yS0veGyqyggcSNzoCQY0NkdDJdAqh64KT7PYPYiGpXGUxVSPVQWZ---RuTa2j8IK1zdrEowqyVjIAAAAATLLfbUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5409036842:AAH4Rgolat3K9mWGdVGZRxMhOQ_JGWD96ak")
BOT_NAME = getenv("BOT_NAME", "M")
API_ID = int(getenv("API_ID", "13814219"))
API_HASH = getenv("API_HASH", "63c10cdc0f579b9e95d4ebfa9484b8cd")
OWNER_NAME = getenv("OWNER_NAME", "sally")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SSaLi")
ALIVE_NAME = getenv("ALIVE_NAME", "sally")
BOT_USERNAME = getenv("BOT_USERNAME", "ADDFAFXbot")
OWNER_ID = getenv("OWNER_ID", "5306882974")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "IRIIRll")
GROUP_SUPPORT = getenv("Dl777l", "xl444")
UPDATES_CHANNEL = getenv("TlTT5", "xl444")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
