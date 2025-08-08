

const DEFAULT_URL = "http://127.0.0.1:8000/";
const get_skills = "profile_get_skills/";

export class Api {


    static async getSkills(login) {
        try {
            const response = await fetch(DEFAULT_URL+get_skills+login);
            return response.data;
        } catch (error) {
            console.error('Ошибка:', error);
            alert('Не удалось загрузить данные');
            return NaN
        }

    }
}