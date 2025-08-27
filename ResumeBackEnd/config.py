from configparser import ConfigParser
from get_env import get_start_patch

config_path = f'{get_start_patch()}ResumeBackEnd/config.ini'

parser = ConfigParser()




"""
Модуль для проверки конфигурационных файлов

"""


def get_db_params(filename=config_path, section='postgresql'):
    parser.read(filename, "utf-8")

    print(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Ошибка подключения к БД! Секция {section} не найдена в файле {filename}'.format(section, filename))

    return db
