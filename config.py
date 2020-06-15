import os

HOST = os.getenv('RDS_HOSTNAME')
PORT = os.getenv('RDS_PORT')
DB_NAME = os.getenv('RDS_DB_NAME')
USER = os.getenv('RDS_USERNAME')
PASSWORD = os.getenv('RDS_PASSWORD')

DATABASE_CONNECTION_URI = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
