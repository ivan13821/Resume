

const DEFAULT_URL = document.getElementById("url").textContent

export class Api {

    // функция для работы с api
    static async getData(login, url) {
        try {
        const response = await fetch(`${DEFAULT_URL}${url}${login}`);
        
        // Проверяем статус ответа
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        // Проверяем Content-Type
        const contentType = response.headers.get('content-type');
        console.log('Content-Type:', contentType);
        
        if (!contentType || !contentType.includes('application/json')) {
            throw new Error('Ответ не в JSON формате');
        }
        
        const data = await response.json();
        return data;
        
    } catch (error) {
        console.error('Полная ошибка:', error);
        return null;
    }
}

    // ------------------------- функция для проверки api -----------------------------
    static async fetchUserData(path, login) {
    try {
        console.log('Начало запроса...');
        
        const response = await fetch(`${path}/${login}`);
        console.log('Response status:', response.status);
        console.log('Response headers:', Object.fromEntries([...response.headers]));
        
        // Проверяем статус ответа
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        // Проверяем Content-Type
        const contentType = response.headers.get('content-type');
        console.log('Content-Type:', contentType);
        
        if (!contentType || !contentType.includes('application/json')) {
            throw new Error('Ответ не в JSON формате');
        }
        
        const data = await response.json();
        console.log('Полученные данные:', data);
        
        return data;
        
    } catch (error) {
        console.error('Полная ошибка:', error);
        return null;
    }
}
}