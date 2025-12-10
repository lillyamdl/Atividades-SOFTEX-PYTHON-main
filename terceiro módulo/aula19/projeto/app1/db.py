from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    "host": os.getenv("db_host", "local_host"),
    "user": os.getenv("db_user", "root"),
    "password": os.getenv("db_pass", ""),
    "database": os.getenv("db_name", "escola_demo"),
    "port": int(os.getenv("db_port", 3306)),
    "charset": "utf8mb4"
}

class Database:
    """Classe simples que abre e fecha conexão"""
    def get_connection(self):
        return connector.connect(**db_config)