import { Api as api } from "../api/apiMain.js"

function checkType(data) {
    if (Array.isArray(data)) {
        return 'array';
    } else if (typeof data === 'object' && data !== null) {
        return 'object';
    } else {
        return 'other';
    }
}




// функция для отрисовки кнопок со скилами
async function createButtons(containerId, data) {

    const container = document.getElementById(containerId);
    container.innerHTML = '';
    let more;

    Object.entries(data).forEach(([head, body]) => {
        const modalId = `modal-$-${head.toLowerCase()}`;
        const userElement = document.createElement('div');
        userElement.className = 'user-skill'

        // создании надписи внутри окна
        if (Array.isArray(body.more)) {
            if (head === 'Еще') {
                more = `Другии технологии: <b>${body.more ? body.more.join(', ') : 'Нет информации'}</b>`;
            } else {
                more = `Связанные технологии: <b>${body.more ? body.more.join(', ') : 'Нет информации'}</b>`;
            }
        } else {
            more = body.more ? body.more : 'Нет информации';
        }

        // создание контаинера 
        userElement.innerHTML = `
        <div class="container">
            <button class="btn" data-modal="${modalId}">${head}</button>
        </div>
        <div id="${modalId}" class="modal-window">
            <div>
                <h1>${head}</h1>
                <button class="modal-close"><h1>&#65794;</h1></button>
                <div>
                    ${more}
                </div>
            </div>
        </div>`;
        container.appendChild(userElement);

        // Добавляем обработчик для открытия модального окна
        const openBtn = userElement.querySelector('.btn');
        const modal = userElement.querySelector('.modal-window');
        
        openBtn.addEventListener('click', function() {
            modal.style.visibility = 'visible';
            modal.style.opacity = '1';
            modal.style.pointerEvents = 'auto';
        });
        
        // Добавляем обработчик для кнопки закрытия
        const closeBtn = userElement.querySelector('.modal-close');
        
        closeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            // Скрываем модальное окно
            modal.style.visibility = 'hidden';
            modal.style.opacity = '0';
            modal.style.pointerEvents = 'none';
            
            // Очищаем URL от хэша
            history.pushState('', document.title, window.location.pathname + window.location.search);
        })
    });
}





// функция получает данные по навыкам и делегирует отрисовку кнопок
async function createSkills(login) {
    let data = await api.getData(login, "profile_get_skills/");
    createButtons('skills-container', data, 'Навыки');
}

// функция получает данные по прочитанным книгам и делегирует отрисовку кнопок
async function createBooks(login) {
    let data = await api.getData(login, "profile_get_books/");
    createButtons('books-container', data);
}

// функция получает данные по опыту пользователя и делегирует отрисовку кнопок
async function createExperience(login) {
    let data = await api.getData(login, "profile_get_experience/");
    createButtons('experience-container', data);
}

// функция получает данные по пет-проектам и делегирует отрисовку кнопок
async function createWorks(login) {
    let data = await api.getData(login, "profile_get_works/");
    createButtons('works-container', data);
}


// функция получает данные по образованию и делегирует отрисовку кнопок
async function createEducation(login) {
    let data = await api.getData(login, "profile_get_education/");
    createButtons('education-container', data);
}







async function init() {

    // Запуск функции для отрисовки кнопок со скилами
    const login =document.getElementById("login").textContent
    await createSkills(login)
    await createBooks(login)
    await createExperience(login)
    await createWorks(login)
    await createEducation(login)
}



init()



