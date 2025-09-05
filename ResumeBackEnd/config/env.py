import os




class Env:
    """ Класс для получения переменных окружения """

    @staticmethod
    def start_patch() -> str:
        """Отдает стартовый путь до папки ResumeBackEnd не включая ее"""

        this_file = os.path.abspath(__file__).split('/') #Путь до этого файла
        path_to_start_project = '/'.join(this_file[0:this_file.index("ResumeBackEnd")]) + "/" #Путь до начала проекта

        return path_to_start_project

    @staticmethod
    def host() -> str:
        """Отдает значение хоста из переменных окружения"""

        return os.getenv("HOST", "0.0.0.0")



    @staticmethod
    def port() -> int:
        """Отдает значение порта из переменных окружения"""

        return int(os.getenv("PORT", 8000))



    @staticmethod
    def database_host() -> str:
        """Отдает значение хоста для подключения к базе данных"""

        return os.getenv("DATABASE_HOST", "localhost")

    @staticmethod
    def back_ip() -> str:
        """"""

        return os.getenv("BACK_IP", "localhost")

