import os

class Env:
    """ Класс для получения переменных окружения """

    @staticmethod
    def start_patch() -> str:
        """Отдает стартовый путь до папки ResumeBackEnd не включая ее"""

        this_file = os.path.abspath(__file__).split('/')
        path_to_start_project = '/'.join(this_file[0:this_file.index("ResumeBackEnd")]) + "/"

        return path_to_start_project

    @staticmethod
    def host() -> str:
        """Отдает значение хоста из переменных окружения"""

        return os.getenv("HOST", "0.0.0.0")



    @staticmethod
    def port() -> int:
        """Отдает значение порта из переменных окружения"""

        return int(os.getenv("PORT", 8000))

