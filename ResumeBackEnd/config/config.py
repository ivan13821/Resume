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

        #Создает массив конфигурационных данных
        for param in params:
            db[param[0]] = param[1]

        #Указывает хост БД. Нужно для безпроблемного запсука с локального ПК и Docker
        db["host"] = Env.database_host()
    else:
        raise Exception(f'Ошибка подключения к БД! Секция {section} не найдена в файле {filename}'.format(section, filename))

    return db
