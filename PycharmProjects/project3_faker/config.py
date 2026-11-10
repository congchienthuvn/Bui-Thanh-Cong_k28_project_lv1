import os
from configparser import ConfigParser


def load_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Không tìm thấy file cấu hình: {filename}")

    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Không tìm thấy section '{section}' trong file {filename}")

    return db

params = load_config()
DB_URL = f"host={params['host']} port=5432 dbname={params['database']} user={params['user']} password={params['password']}"