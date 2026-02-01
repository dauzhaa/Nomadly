# Nomadly

## Описание
Nomadly — это цифровая платформа (e-commerce) дизайнерской одежды, посвященная сохранению культурного кода. Проект трансформирует опыт покупки, объединяя современный ритейл с историческим сторителлингом (Shop by Meaning).

В техническом плане это **Monolith**, построенный на принципах модульности и чистого кода, с гибридным управлением состоянием (Redis + DB) и асинхронными задачами.

## Стек технологий

### Backend
- **Framework**: Django 5.1, Django REST Framework (DRF)
- **Language**: Python 3.12+
- **Database**: PostgreSQL (реляционные данные)
- **Cache & Session**: Redis (корзина, кэш API, брокер задач)
- **Asynchronous**: Celery (отправка email, фоновые задачи)
- **Images**: Pillow

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Server**: Gunicorn / Nginx (планируется)

## Архитектура (Модули)
Проект разделен на независимые Django-приложения (Components):
- **Core**: Общие утилиты, абстрактные модели.
- **Users**: Кастомная авторизация, профили.
- **Catalog**: Управление товарами (Product) и категориями.
- **Content**: Культурные мотивы (Motifs), истории, связь с товарами.
- **Cart**: Логика корзины (Session-based + Redis hybrid).
- **Orders**: Оформление заказа, жизненный цикл.
- **Payments**: Интеграция с Kaspi Pay.

## Установка и запуск (Local Development)

### Вариант A: Через Docker (Рекомендуется)
Для запуска всего окружения (Backend + DB + Redis):

1. Создайте файл `.env` в корне (см. `.env.example`).
2. Запустите сборку:
   ```bash
   docker compose up --build
