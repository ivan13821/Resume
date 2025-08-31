from configparser import ConfigParser
from config.env import Env

config_path = f'{Env.start_patch()}ResumeBackEnd/config.ini'

parser = ConfigParser()




"""
Модуль для проверки конфигурационных файлов

"""


def get_db_params(filename=config_path, section='postgresql'):
    """Проверяет наличие postgres в файле config.ini"""

    parser.read(filename, "utf-8")

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Ошибка подключения к БД! Секция {section} не найдена в файле {filename}'.format(section, filename))

    return db
