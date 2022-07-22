import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

ADMIN_ID = os.getenv('ADMIN_ID')

GROUP_ID = os.getenv('GROUP_ID')