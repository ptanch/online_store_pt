# Интернет-магазин (Django + Poetry)

Учебный проект интернет-магазина на **Django**, управляемый через **Poetry**.  
Цель — освоить Django и постепенно развивать функционал от базовой структуры до полноценного приложения.

---

## ⚙️ Стек технологий
- Python 3.x
- Django
- Poetry (для управления зависимостями и окружением)
- Bootstrap (для верстки шаблонов)

---

## 📂 Текущая структура проекта
```
online_store_pt/
├── catalog/ # Приложение "Каталог"
│ ├── migrations/ # Миграции БД
│ ├── templates/ # HTML-шаблоны приложения
│ │ ├── contacts.html
│ │ └── home.html
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── config/ # Основной проект Django (настройки)
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3 # База данных (SQLite)
├── manage.py # Скрипт управления проектом
├── poetry.lock # Lock-файл Poetry
├── pyproject.toml # Конфигурация Poetry
└── README.md
```

## 🚀 Реализовано
- Настроен проект Django через Poetry.  
- Создано приложение `catalog`.  
- Настроена маршрутизация для приложения.  
- Подготовлены HTML-шаблоны:
  - `home.html`
  - `contacts.html`  
- Реализованы контроллеры для отображения страниц.  
- Настроена обработка данных формы в контроллере:
  - при успешной отправке формы отображается сообщение об успехе.

---

## ▶️ Запуск проекта
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/username/online-store-pt.git
   cd online-store-pt
   
2. Установить зависимости через Poetry:
```
poetry install
```

3. Активировать виртуальное окружение:
```
poetry shell
```

4. Выполнить миграции:
```
python manage.py migrate
```

5. Запустить сервер разработки:
```
python manage.py runserver
```

После запуска проект будет доступен по адресу:
👉 http://127.0.0.1:8000/home/ или http://127.0.0.1:8000/contacts/