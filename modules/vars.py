#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "13076045"))
API_HASH = environ.get("API_HASH", "32f2036dcb66c94637a7e87de6b6001b")
BOT_TOKEN = environ.get("BOT_TOKEN", "8260420940:AAH6fYs8MyxQzZ8zNve5Lfll4XRsw9HPi0E")

OWNER = int(environ.get("OWNER", "1801203400"))
CREDIT = environ.get("CREDIT", "𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8222519141').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1801203400').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
