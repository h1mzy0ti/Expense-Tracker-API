# 📒 Expense Tracker API

A Django REST Framework backend for tracking user expenses. It supports JWT authentication, expense creation, date filtering, and powerful analytics.

---

## ✨ Features

* 🔐 JWT-based authentication (djangorestframework-simplejwt).
* ✅ Protected routes requiring a valid token.
* 🧾 Expense creation with rich fields (category, description, payment method).
* 📆 Date-range filtering.
* 📊 Analytics: total expenses, category breakdown, daily/weekly/monthly trends.
* 📜 Interactive API docs with Swagger.

---

## ⚙️ Tech Stack

* **Backend:** Django REST Framework
* **Auth:** JWT (simplejwt)
* **Database:** SQLite (minimal setup)
* **ORM:** Django ORM
* **Docs:** Swagger (drf-yasg)

---

## 📑 Models

### 🧑‍💼 User

* id
* username
* email
* password (managed via Django's built-in User model)

### 💰 Expense

* id
* amount
* category
* description
* payment\_method (e.g. cash, card, UPI)
* date
* user (ForeignKey to User)

---

## 🔗 API Endpoints

### 🗝️ Auth

* **POST /api/signup/**: Register new user
* **POST /api/login/**: Obtain JWT token
* **POST /api/logout/**: Logout and blacklist refresh token

### 💵 Expenses

* **POST /api/expenses/**: Create new expense
* **GET /api/expenses/**: List expenses (filter by `start_date` and `end_date`)
* **GET /api/expenses/analytics/**:

  * Total expenses
  * Category-wise breakdown
  * Daily/Weekly/Monthly trends

---

## 🔐 Authentication

All routes except `/signup/` and `/login/` require a **JWT Access Token**.

Include in headers:

```
Authorization: Bearer <access_token>
```

---

## 📜 Interactive Documentation

Swagger UI available at:

```
http://127.0.0.1:8000/swagger/
```

---

## 🚀 Getting Started

Run this project locally in two ways:

---

### ⚡ Option 1: Complete Setup (Recommended)

1. **Clone the repo**

   ```
   git clone https://github.com/h1mzy0ti/Expense-Tracker-API.git
   cd expense_tracker_api
   ```

2. **Create and activate virtual environment**

   ```
   python -m venv venv
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   ```
   python manage.py createsuperuser
   ```

6. **Start the server**

   ```
   python manage.py runserver
   ```

7. **Access**

   * Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
   * API Base: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

### ⚡ Option 2: Using Provided venv (Ultra-Minimal Setup)

1. **Clone the repo**

   ```
   git clone https://github.com/h1mzy0ti/Expense-Tracker-API.git
   cd expense_tracker_api
   ```

2. **Activate the provided virtual environment**

   ```
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate          # Windows
   ```

3. **Run the server directly**

   ```
   python manage.py runserver
   ```

4. **Access**

   * Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
   * API Base: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

> *Note:* Since SQLite is used, no DB setup is needed, and you can run immediately after activating venv.

---

## 📌 Endpoint Usage Guide

### 🗝️ POST /api/signup/

Register a new user.

**Request Body:**

```json
{
  "username": "exampleuser",
  "email": "user@example.com",
  "password": "yourpassword"
}
```

**Expected Response:**

```json
{
  "id": 1,
  "username": "exampleuser",
  "email": "user@example.com"
}
```

---

### 🗝️ POST /api/login/

Obtain JWT access and refresh tokens.

**Request Body:**

```json
{
  "username": "exampleuser",
  "password": "yourpassword"
}
```

**Expected Response:**

```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

---

### 🗝️ POST /api/logout/

Blacklist refresh token to logout.

**Request Body:**

```json
{
  "refresh": "your-refresh-token"
}
```

**Expected Response:**

```json
{
  "message": "Logged out successfully"
}
```

---

### 💵 POST /api/expenses/

Create a new expense.

**Request Body:**

```json
{
  "amount": 150.75,
  "category": "Food",
  "description": "Lunch at cafe",
  "payment_method": "Card",
  "date": "2025-07-10"
}
```

**Expected Response:**

```json
{
  "id": 1,
  "amount": 150.75,
  "category": "Food",
  "description": "Lunch at cafe",
  "payment_method": "Card",
  "date": "2025-07-10",
  "user": 1
}
```

---

### 📆 GET /api/expenses/

List expenses (supports date filtering).

**Query Parameters:**

```
start_date=YYYY-MM-DD
end_date=YYYY-MM-DD
```

**Example Request:**

```
/api/expenses/?start_date=2025-07-01&end_date=2025-07-31
```

**Expected Response:**

```json
[
  {
    "id": 1,
    "amount": 150.75,
    "category": "Food",
    "description": "Lunch at cafe",
    "payment_method": "Card",
    "date": "2025-07-10",
    "user": 1
  }
]
```

---

### 📊 GET /api/expenses/analytics/

Returns expense analytics.


**Expected Response:**

```json
{
  "total_expense": 2500.00,
  "category_breakdown": [
    {"category": "Food", "total": 1200.00},
    {"category": "Travel", "total": 800.00}
  ],
  "daily_trends": [
    {"day": "2025-07-10", "total": 150.75}
  ],
  "weekly_trends": [
    {"week": "2025-07-07", "total": 800.00}
  ],
  "monthly_trends": [
    {"month": "2025-07-01", "total": 2500.00}
  ]
}
```

---

## 📝 Notes

* SQLite ensures minimal setup and local running out of the box.
* All expense routes require JWT authentication.
* Instructions and dependencies included for easy testing.
