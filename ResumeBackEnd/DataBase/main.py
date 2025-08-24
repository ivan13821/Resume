import psycopg2
from config import get_db_params


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance



@singleton
class Database:

    # подключение и создание бд ------------------------------------------------------------------------------------------
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()

    def connect_to_db(self):
        params = get_db_params()
        print('Подключаюсь к PostgreSQL...')
        try:
            self.conn = psycopg2.connect(**params)
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            print(f'Успешно подключен!')
        except Exception as error:
            print(error)




    def execute_query(self, query, params=None):
        try:
            if params is not None:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
        except psycopg2.InterfaceError as e:
            print(e)
            print("Не удалось выполнить запрос из-за ошибки подключения. Пытаюсь подключиться к базе заново")
            self.connect_to_db()
            self.cur.execute(query, params)


    # Работа с БД ----------------------------------------------------------------------------------------------



    def get_profile(self, login):

        """Отдает данные о профиле пользователя по логину"""

        self.execute_query(f"select * from profile where login='{login}'")

        return self.cur.fetchall()



    def get_skills(self, login):

        """Возвращает скилы пользователя"""

        self.execute_query(f"select skill, level, more from skills where login='{login}'")

        return self.cur.fetchall()

    def get_books(self, login):

        """Возвращает книги прочитанные пользователем пользователя"""

        self.execute_query(f"select name, author, more from books where login='{login}'")

        return self.cur.fetchall()


    def get_experience(self, login):

        """Возвращает опыт работы пользователя"""

        self.execute_query(f"select company, more from experience where login='{login}'")

        return self.cur.fetchall()

    def get_works(self, login):

        """Возвращает опыт работы пользователя"""

        self.execute_query(f"select name, more from my_works where login='{login}'")

        return self.cur.fetchall()

    def get_education(self, login):

        """Возвращает опыт работы пользователя"""

        self.execute_query(f"select name, more from education where login='{login}'")

        return self.cur.fetchall()