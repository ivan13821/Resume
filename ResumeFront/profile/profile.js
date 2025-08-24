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
    console.log(data)

    Object.entries(data).forEach(([head, body]) => {
        const modalId = `modal-$-${head.toLowerCase()}`;
        const userElement = document.createElement('div');
        userElement.className = 'user-skill'
        if (Array.isArray(body.more)) {
            more = body.more ? body.more.join(', ') : 'Нет информации';
        } else {
            more = body.more;
        }
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

async function createBooks(login) {
    let data = await api.getData(login, "profile_get_books/");
    createButtons('books-container', data);
}

// async function createExperience(login) {
//     let data = await api.getSkills(login);
//     createButtons('skills-container', data);
// }








async function init() {

    // Запуск функции для отрисовки кнопок со скилами
    const login =document.getElementById("login").textContent
    await createSkills(login)
    await createBooks(login)
}



init()



