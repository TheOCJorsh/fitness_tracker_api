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

## 🚀Week 2 — Activity System Setup.
## Activity model (for milestone) - CRUD APIs - Users Permissions - Test run.
Here is what was accomplished in this week.

## Implemented the Activity model with fields.

activity_type | duration_minutes | distance_km | calories_burned
activity_date | notes | created_at | user (ForeignKey relationship)

## CRUD API endpoints set up for users activities.

Create activity | View activities | Update activity | Delete activity

## JWT Authentication using SimpleJWT

User login endpoint (/api/token/)
Token refresh endpoint (/api/token/refresh/)
Secured endpoints with authentication permissions

## Testing
Successfully tested all endpoints using REST Client inside VS CODE

## Clean Repo Update
Pushed progress to GitHub Repository

## Challenges and solutions

Challenge: Token authentication errors (expired or invalid token)

Solution:
- Adjusted token refresh endpoint up to 1 hour
- Properly configured authentication headers:
  Authorization: Bearer <access_token>

## 🚀Week 3 — Milestone System and Community setup
Exciting features were implemented this week.

## Milestone filtering
Milestone filter for users activities was implemented using date:

Daily milestones | Weekly milestones | Monthly milestones

Using the in-built Django ORM date filtering for efficient queries

## Users activity streak system

Implemented streak calculation endpoint:

GET /api/activities/streak/

This calculates consecutive active days per user

## Community feature implementation

Created new models for users activities such as:
Post model | Comment model | Like model

## Established proper relationships between.

- User → Post
- Post → Comment
- Post → Like

## Implemented endpoints for:

Creating community posts | Viewing posts | Liking posts | Commenting on posts | Viewing post engagements

## Multiple user setup for community testing.

Created multiple users:
FitAdmin | mike24 | maryqueen | martins

Successfully tested:
- Cross-user likes
- Cross-user comments
- Community engagement system


