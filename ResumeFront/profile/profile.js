import { Api as api } from "../api/apiMain.js"





// функция для отрисовки кнопок со скилами
async function createSkills(login) {

    let data = await api.getSkills(login)


    const container = document.getElementById('skills-container');
    container.innerHTML = '';
    console.log(data)

    Object.entries(data).forEach(([skillName, skillData]) => {
        const modalId = `modal-$-${skillName.toLowerCase()}`;
        const userElement = document.createElement('div');
        userElement.className = 'user-skill'
        userElement.innerHTML = `
        <div class="container">
            <button class="btn" data-modal="${modalId}">${skillName}</button>
        </div>
        <div id="${modalId}" class="modal-window">
            <div>
                <button class="modal-close"><h1>&#65794;</h1></button>
                <br>
                <h1>${skillName}</h1>
                <div>
                    ${skillData.related_skills ? skillData.related_skills.join(', ') : 'Нет связанных навыков'}
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
        });
    });
}

async function init() {

    // Запуск функции для отрисовки кнопок со скилами
    const login =document.getElementById("login").textContent
    await createSkills(login)
}



init()



