import os
from sqlalchemy import *


DB_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:sesame@localhost/amazonmusicalins2?charset=utf8')
