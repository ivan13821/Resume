



create table profile(
	login text unique not null primary key,
	name text not null,
	surname text not null,
	about_human text not null,
	date_of_bithday date not null,
	phone varchar(20) not null,
	mail text not null,
	tg_login text
);




create table skills (
	skils_id SERIAL PRIMARY key,
	level integer not null CHECK (level IN (1, 2, 3)),
	skill text not null,
	more text[],
	
	login text REFERENCES profile(login) ON DELETE RESTRICT
);




create table books (
	book_id serial primary key,
	name text,
	author text,
	more text,
	
	login text REFERENCES profile(login) ON DELETE RESTRICT
);


create table experience (
	id serial primary key,
	company text,
	more text,
	
	login text REFERENCES profile(login) ON DELETE RESTRICT
);


create table my_works (
	id serial primary key,
	name text,
	more text, 
	
	login text REFERENCES profile(login) ON DELETE RESTRICT
);


create table education (
	id serial primary key,
	name text,
	more text, 
	
	login text REFERENCES profile(login) ON DELETE RESTRICT
);




insert into profile (
login, name, surname, about_human, date_of_bithday, phone, mail, tg_login
) values (
'ivashka', 'Иван', 'Сафаров', 'Я стараюсь всегда совершенствоваться в своих навыках и знаниях. Для меня важно работать над сложными и интересными проектами. Я не боюсь трудностей, которые с этим связанны, наоборот, мне они нравятся. Стараюсь создавать не просто код, а удобное, масштабируемое и понятное решение для сервисов.', '2006-06-08', '89967209618', 'safarovi670@gmail.com', '@ivashka138'
);

insert into profile (
login, name, surname, about_human, date_of_bithday, phone, mail, tg_login
) values (
'angel', 'Ангелина', 'Землянская', 'Я творческая личность, мои руки всегда заняты делом', '2005-07-23', '89018038060', 'safarovi670@gmail.com', '@ivashka138'
);



insert into books (
name, author, login, more) values 
('Паттерны проетирования', 'Эрик Фримен', 'ivashka', 'Паттерны проектирования Эрика Фримена — это классика в мире ООП. Книга из знаменитой серии Head First, где сложные концепции объясняются через визуалы, диалоги и юмор. Она учит применять 23 основных паттерна (как Стратегия, Наблюдатель, Фабрика) для создания гибкого и переиспользуемого кода. Идеально для разработчиков, которые хотят проектировать системы, а не просто писать код.'),
('Алгоритмы', 'Грокаем', 'ivashka', 'Грокаем алгоритмы Адитьи Бхаргавы — это практическое и наглядное введение в алгоритмы и структуры данных. Книга известна своим простым языком, понятными иллюстрациями и примерами из реальной жизни. Она идеально подходит для начинающих, помогая понять основы — от бинарного поиска и сортировки до более сложных тем вроде графов и динамического программирования. Автор делает акцент на интуитивном понимании, а не на сухой теории, что позволяет легко освоить алгоритмическое мышление. Отличный старт для всех, кто готовится к собеседованиям или хочет стать сильнее в программировании.'),
('Чистый код', 'Роберт мартин', 'ivashka', 'Чистый код Роберта Мартина (дядя Боб) — это библия для разработчиков, стремящихся писать не просто работающий, но и качественный код. Книга отвечает на главный вопрос: как создавать код, который будет легко читать, понимать и поддерживать.

Мартин детально разбирает принципы, паттерны и практики написания чистого кода. Он учит правильно именовать переменные, структурировать функции, обрабатывать ошибки, писать тесты и проектировать классы. Основная мысль: код должен быть написан для людей, а не для машин.

Книга наполнена конкретными примерами — от плохого кода к хорошему, что позволяет наглядно увидеть разницу. Это must-read для любого серьёзного программиста, который хочет расти как профессионал и создавать системы, которые живут долго и стоят дёшево в поддержке.');



insert into experience (
company, more, login
) values 
('СГЭУ', '<p>В СГЭУ я работал программистом</p>
<p>За время работы создал: вопросно-ответную систему, сервис для автоматического создания pdf документов</p>
<p>Работал с технологиями: Java, Git, Docker, Python, aiogram, spring, HTML, CSS, JS</p>', 'ivashka'),
('Яндекс', '<p>В Яндекс я продолжаю работать инженером технической поддержки Yandex Cloud</p>
<p>За время работы ознакомился с множеством сервисов, и понимаю как они работают: ВМ, kuber, datalens, MDB, API, S3, DNS и далее</p>', 'ivashka'),
('Открытый код', '<p>Проходил стажировку в компании открытый код</p>
<p>За время стажировки я ознакомился с unit-тестированием</p>', 'ivashka');


insert into my_works (
name, more, login
) values 
('Вопросно-ответная система', '<p><a href="https://github.com/ivan13821/BOT_USD">Моя вопросно-ответная система</a> основана на алгоритме. Она позволяет пользователю обратиться с вопросом, и, если немного похожий вопрос был задан раньше, то она даст ответ в автоматическом режиме.</p>
<p>Она позволяет автоматизировать рутинные задачи единого студенческого департамента. Также редактирование ответов после изменений в университете легкое.</p>
<p>При создании этой системы я использовал технологии: <b>Git, Docker, Python, SQL</b></p>', 'ivashka'),
('Онлайн компилятор', '<p><a href="https://github.com/ivan13821/OnlineCompilator">Онлайн компилятор</a> позволяет запускать код в браузере. Код отправляется на сервер и запускается там, а пользователь получает ответ.</p>
<p>Отмечу, что этот проект еще находится в стадии разработки.</p>
<p>При создании этого сервиса я использовал технологии: <b>Git, Python, JS, CSS, HTML, API, pydantic, fastapi</b></p>', 'ivashka'),
('Резюме', '<p><a href="https://github.com/ivan13821/Resume">Резюме</a>, которое вы сейчас читаете, я старался создавать, чтобы его было максимально удобно масштабировать и рефакторить. Создал я его для того, чтобы потренироваться в навыках и повысить удобство работодателей. (Хочу отметить, что тут не только мое резюме.)</p>
<p>При создании этого сайта я использовал технологии: <b>Git, Docker, Python, JS, CSS, HTML, API, pydantic, fastapi, serverless (размещение в облаке)</b></p>', 'ivashka');





insert into skills (
skill, level, more, login
) values
('Python', 3, array['fastapi', 'асинхронное программирование', 'aiogram3', 'psycopg'], 'ivashka'),
('SQL', 2, array['PostgreSQL', 'MySQL'], 'ivashka'),
('Java', 1, array['spring'], 'ivashka'),
('JS', 1, array['vue'], 'ivashka'),
('C++', 1, null, 'ivashka'),
('Еще', 2, array['html', 'css', 'Git', 'Docker', 'datalens', 'linux', 's3'], 'ivashka');


insert into education (
name, more, login
) values 
('СГЭУ', '<p>Учусь по направлению: прикладная информатика и защита информации.</p>
<p>Учится начал в 2023 году, а закончу в 2027.</p>', 'ivashka'),
('Stepik', '<p>Проходил множество курсов, подробнее о них вы можете посмотреть в моем <a href="https://stepik.org/users/298483336/profile">профиле</a>.</p>', 'ivashka');



--update profile
--set about_human='Я стараюсь всегда совершенствоваться в своих навыках и знаниях. Для меня важно работать над сложными и интересными проектами. Я не боюсь трудностей, которые с этим связанны, наоборот, мне они нравятся. Стараюсь создавать не просто код, а удобное, масштабируемое и понятное решение для сервисов.'
--where login='ivashka';


-- DANGER ZONE 	

--delete from skills;
--drop table books;


insert into profile (
login, name, surname, about_human, date_of_bithday, phone, mail, tg_login
) values (
'ninka', 'Нина', 'Шишкина', 'Я творческая личность', '1980-04-06', '89222560904', 'ninka-sardinka@mail.ru', '@ninel'
);


insert into experience (
company, more, login
) values 
('Маникюр', '<p>Занимаюсь маникюром более 10 лет!</p>
<p>За это время изучила множество техник и ...</p>', 'ninka');



