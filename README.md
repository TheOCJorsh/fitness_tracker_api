# 🏋️AI Fitness Tracker & Community API.

## 📌 Project Overview

The idea for this project is to build an app for my brother who is a Fitness Coach and it will allow users to:
Track their fitness activities
View performance milestones based on daily, weekly and monthly.
Share those milestones in a community feed.
Interact socially (comments & reactions)
Receive AI workout insights based on their performance data

This project is a built with Django and Django REST Framework.  

---

## 🚀 Week 1 Progress Status
## Structure & Foundation Setup

The following features and configurations have been completed:

### ✅ 1. Project Setup & Installations.
- Created virtual environment
- Created My Django project (`config`)

- Installed required dependencies:
  - Django
  - Django REST Framework
  - Simple JWT (Authentication)
  - psycopg2-binary (PostgreSQL driver)
i also generated `requirements.txt`

---

### ✅ 2. App Setup.

I have structured the project into 3 Django apps for clean development:

- users → Handles authentication & user management
- activities → Will handle activity tracking & milestone calculations
- community → Will handle milestone sharing, comments, and reactions

---

### ✅ 3. JWT Authentication System Setup.

Configured JWT authentication using `djangorestframework-simplejwt`.

Available endpoints:

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | `/api/register/` | Register new user |
| POST | `/api/token/` | Obtain access & refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |

JWT authentication is required for each route.

---

### ✅ 4. Git Setup & Project Push

- Git repository initialized
- Proper `.gitignore` created
- Clean commit history maintained
- Project pushed to GitHub

---

## 🛠 Here are my Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication
- Git & GitHub

---

## Week 2 — Activity System Setup [ Coming soon]
## Activity model (for milestone) - CRUD APIs - Users Permissions - Test run.


