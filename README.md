# SchoolBellSystem
Документ по проектированию веб-сервиса "Система для школьных звонков"
1. Введение
Название: Система для школьных звонков
Описание: Сервис, позволяющий создавать и менять расписание звонков, добавлять и удалять звонки в конкретные дни, а также загружать звуки для звонков.
Целевая аудитория: Администрация школы.
2. Анализ требований
Функциональные требования
•	Создание и изменение расписания.
•	Добавление и удаление звонков.
•	Выбор звука для звонка.
•	Загрузка нового звука.
•	Вход с паролем.
Нефункциональные требования
•	Должно работать слабом компьютере и не тратить много производительности.
•	Простой и дружелюбный интерфейс.
3. Концепция пользовательского интерфейса (UI/UX)
Основные страницы:
•	Стандартное расписание звонков (Добавление и удаление звонков, изменение звуков).
•	Расписание на конкретный день (Добавление и удаление звонков, изменение звуков).
•	Загрузка нового звука в базу данных.
Пользовательские сценарии:
1.	Пользователь заходит на сервис и удаляет звонок из стандартного расписания.
2.	Пользователь загружает новый звук на сервис.
3.	Пользователь добавляет новый звонок с новым звуком только на следующий день.
4. Архитектура системы
Технологии:
•	Frontend: jinja2 (для динамичного интерфейса).
•	Backend: Flask (обрабатывает запросы, хранит данные).
•	База данных: SQLite (хранит пользователей, посты, лайки).
Структура базы данных:
•	Sounds (id, name, file (mp3)).
•	Bells (id, day_id, sound_id, time).
API (основные запросы):
•	POST /login – вход в систему.
•	GET /days – получение списка дней.
•	GET /days/{n} – получение расписания в день n.
•	POST /days/{n}/add – добавление звонка в день n.
•	DELETE /days/{n}/{m}/delete – удаление m звонка в день n.
•	POST /sound – добавление звука.
5. План разработки
•	Конец марта: Полный дизайн интерфейса.
•	Середина апреля: Разработка backend, база данных.
•	Конец апреля: Разработка frontend (страницы, формы).
•	Начало мая: Работа со звуками.
•	Середина мая: Тестирование, исправление багов.
6. Итоговые выводы и перспективы
•	Базовая версия облегчит работу со звонками для администрации школы.
•	В будущем нужно сделать работу с расписанием более удобной.
