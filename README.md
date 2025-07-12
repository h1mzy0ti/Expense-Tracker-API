# Expense Tracker API

A Django REST Framework backend for tracking user expenses. It supports JWT authentication, expense creation, filtering by date, and powerful analytics.

---

## Features

* JWT-based authentication (djangorestframework-simplejwt).
* Protected routes requiring a valid token.
* Expense creation with rich fields (category, description, payment method).
* Date-range filtering.
* Analytics including total expenses, category breakdown, and daily/weekly/monthly trends.
* Interactive API docs with Swagger.

---

## Tech Stack

* **Backend:** Django REST Framework
* **Auth:** JWT (simplejwt)
* **Database:** SQLite (minimal setup)
* **ORM:** Django ORM
* **Docs:** Swagger (drf-yasg)

---

## Models

### User

* id
* username
* email
* password (managed via Django’s built-in User model)

### Expense

* id
* amount
* category
* description
* payment\_method (e.g. cash, card, UPI)
* date
* user (ForeignKey to User)

---

## API Endpoints

### Auth

* **POST /api/signup/**: Register new user
* **POST /api/login/**: Obtain JWT token
* **POST /api/logout/**: Logout and blacklist refresh token

### Expenses

* **POST /api/expenses/**: Create new expense
* **GET /api/expenses/**: List expenses (filter by `start_date` and `end_date`)
* **GET /api/expenses/analytics/**:

  * Total expenses
  * Category-wise breakdown
  * Daily/Weekly/Monthly trends

---

## Authentication

All routes except `/signup/` and `/login/` require a **JWT Access Token**.

Include in headers:

```
Authorization: Bearer <access_token>
```

---

## Interactive Documentation

Swagger UI available at:

```
http://127.0.0.1:8000/swagger/
```

---

## Getting Started

You can run this project locally in two ways:

---

### Option 1: Complete Setup (Recommended)

If you want to set up your own virtual environment:

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

---

### Option 2: Using Provided venv (Ultra-Minimal Setup)

If you want *immediate* local running using the pushed `venv`:

1. **Clone the repo**

   ```
   git clone <your-repo-url>
   cd <your-repo-directory>
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

> *Note:* Since SQLite is used, no DB setup is needed, and you can run immediately after activating venv.

---

## Notes

* SQLite ensures the project requires minimal setup and runs locally out of the box.
* All expense routes are protected and require JWT authentication.
* Usage instructions and dependencies are included for easy local testing.
