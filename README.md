#  Microservices Architecture: Inventory & Order Management

[![API Tests](https://github.com/victoriababala/mprpp-final-task/actions/workflows/api-tests.yml/badge.svg)](https://github.com/ВАШ_ЛОГІН/ВАШ_РЕПОЗИТОРІЙ/actions/workflows/api-tests.yml)

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white"/>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
</p>

---

## 🧩 Project Overview

Цей проєкт демонструє реалізацію **мікросервісної архітектури** для управління запасами та замовленнями.

### 🔹 Основні ідеї:
- Два незалежні мікросервіси
- Взаємодія через HTTP API
- Контейнеризація через Docker
- Оркестрація через Docker Compose
- CI/CD з автоматичним тестуванням API

---

## 🏗️ Architecture

```text
        ┌────────────────────┐
        │   Order Service    │
        │   (порт: 9001)     │
        └─────────┬──────────┘
                  │ HTTP
                  ▼
        ┌────────────────────┐
        │ Inventory Service  │
        │   (порт: 8001)     │
        └────────────────────┘
```

---

## 📁 Project Structure

```bash
microservices_project/
├── .github/workflows/
│   └── api-tests.yml        # CI/CD (GitHub Actions)
├── inventory_service/       # Inventory microservice
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
├── order_service/           # Order microservice
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
├── collection.json          # Postman tests collection
└── docker-compose.yml       # Services orchestration
```

---

## ⚙️ Services & Endpoints

### 📦 Inventory Service (`:8001`)

| Method | Endpoint            | Description                      |
|--------|--------------------|----------------------------------|
| GET    | `/stock/{id}`      | Отримати кількість товару       |
| POST   | `/stock/update`    | Оновити залишки                |

---

### 🧾 Order Service (`:9001`)

| Method | Endpoint   | Description                                  |
|--------|------------|----------------------------------------------|
| POST   | `/orders`  | Створити замовлення (з перевіркою складу)    |
| GET    | `/orders`  | Отримати всі замовлення                      |

---

## 🧪 Testing

API тестування виконується через **Postman Collection** та **Newman**.

### 🔹 Запуск тестів локально:

```bash
npm install -g newman
newman run collection.json
```

---

## 🚀 Getting Started

### 🔧 Передумови:
- Docker
- Docker Compose

### ▶️ Запуск проєкту:

```bash
docker compose up -d --build
```

Після запуску сервіси доступні:
- 📦 Inventory → http://localhost:8001
- 🧾 Orders → http://localhost:9001

---

## 🔄 CI/CD

Проєкт використовує **GitHub Actions** для:
- автоматичного запуску API тестів
- перевірки контрактів між сервісами

---
