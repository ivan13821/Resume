from DataBase.main import Database
import base64


db = Database()



def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string



class Profile:

    @staticmethod
    def get_profile(login):

        """Возвращает данные о профиле в формате JSON"""

        data = db.get_profile(login)

        if not data: return {'error':'profile is invalid'}

        data = data[0]

        tg_login = {}

        if data[7] is not None:
            tg_login = {'tg_login':data[7]}

        profile = {**{
            "login":data[0],
            "name":data[1],
            "surname":data[2],
            'about_profile':data[3],
            'date_of_bithday':data[4],
            'phone':data[5],
            'mail':data[6],
        }, **tg_login}

        return profile



    @staticmethod
    def get_skills(login):

        """Возвращает скилы полльзовтеля в формате JSON"""

        data = db.get_skills(login)

        if data[0] is None:
            return {'error':'profile is invalid'}

        skills = {}

        for skill in data:
            skills[skill[0]] = {
                'level':skill[1],
                'more':skill[2]
            }

        return skills


    @staticmethod
    def get_books(login):

        """Возвращает книги прочитанные пользователем"""

        data = db.get_books(login)

        if data[0] is None:
            return {'error':'profile is invalid'}

        books = {}

        for book in data:
            books[book[0]]= {
                    "name":book[0],
                    "author":book[1],
                    "more":book[2]
                 }

        return books



    @staticmethod
    def get_all(login):

        """Возвращает все данные по логину, используется при загрузке страницы"""

        profile, skills = Profile.get_profile(login), Profile.get_skills(login)

        #Если ошибка есть в профиле, то она будет и в навыках, т.к в БД нельзя добавить навыки без родителя
        if 'error' in profile.keys():
            return profile

        return {
            'profile':profile,
            'skills':skills
        }


