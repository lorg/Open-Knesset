from os import path
from settings import *
DATABASE_ENGINE = 'sqlite3'         # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.

DATABASE_NAME = '/home/daonb/sites/Open-Knesset/project/dev.db'  # Or path to database file if using sqlite3.
LOCAL_DEV = True
MEDIA_URL = '/static/'
MEDIA_ROOT = path.join(PROJECT_ROOT, 'static', '')
