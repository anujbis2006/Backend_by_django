# Project 15 - Django Portfolio App

## 📌 Overview
**Project15** is a Django-based portfolio web application that demonstrates core Django concepts including models, views, templates, URL routing, admin interface customization, and database migrations.

---

## 🧠 Key Learnings

### 1. Django Project Structure
```
project15/
├── manage.py              # Django CLI entry point
├── portfolio/             # Main app
│   ├── models.py          # Database models (Student, Profile)
│   ├── views.py           # View functions (home)
│   ├── urls.py            # App-level URL routing
│   ├── admin.py           # Admin registration for models
│   ├── templates/         # HTML templates
│   └── migrations/        # Database migration files
├── project15/             # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI config for deployment
├── static/                # Static files directory
└── db.sqlite3             # SQLite database
```

### 2. Models & Database
- **Student Model**: `name`, `age`, `city` fields
- **Profile Model**: `bio` (TextField), `location` (CharField), `birth_date` (DateField)
- **`__str__` method**: Custom string representation for admin display
- **Migrations**: `makemigrations` and `migrate` commands to sync models with database

### 3. URL Routing
- **Root URLs** (`project15/urls.py`): Includes app URLs using `include()`
- **App URLs** (`portfolio/urls.py`): Maps URL patterns to view functions
- **Admin URLs**: Built-in Django admin at `/admin/`

### 4. Views & Templates
- **Function-based views**: `home()` renders template with context
- **Template structure**: App templates in `portfolio/templates/portfolio/`
- **Template rendering**: Using `render(request, 'template.html')`

### 5. Admin Interface
- **Model Registration**: Register models in `admin.py` with `admin.site.register()`
- **CRUD Operations**: Full create, read, update, delete via admin panel
- **Admin URL**: `/admin/` with superuser authentication

### 6. Common Errors & Fixes
| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'porfolio'` | Typo in `INSTALLED_APPS` | Correct spelling to `'portfolio'` |
| `no such table: portfolio_student` | Missing or stale migration | Run `makemigrations` then `migrate` |
| `table has no column named location` | Model field added without migration | Create and apply new migration |
| `SyntaxError: '(' was never closed` | Missing closing parenthesis in code | Fix syntax in `models.py` |
| `AttributeError: module 'django.db.models' has no attribute 'c'` | Incomplete field definition | Use full field name like `models.CharField()` |

### 7. Migration Management
1. **Create migrations**: `python manage.py makemigrations`
2. **Apply migrations**: `python manage.py migrate`
3. **Check status**: `python manage.py showmigrations`
4. **Reset migration (if needed)**: 
   - `python manage.py migrate --fake <app> zero`
   - Delete stale migration files
   - Regenerate with `makemigrations`
   - Apply with `migrate`
5. **Database cleanup**: Drop stale tables directly via `python manage.py dbshell`

### 8. Static Files
- Configured in `settings.py` with `STATIC_URL` and `STATICFILES_DIRS`
- Served during development automatically when `DEBUG = True`

### 9. Git & Version Control
- Initialize: `git init`
- Add files: `git add .`
- Commit: `git commit -m "message"`
- Push: `git push origin <branch>`

---

## 🚀 How to Run

```bash
# Navigate to project
cd project15

# Install dependencies (if virtual environment not active)
python -m venv .venv
source .venv/bin/activate

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access
# Main: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```

---

## 🛠️ Tech Stack
- **Backend**: Django 6.0.7
- **Database**: SQLite3
- **Language**: Python 3.14
- **Frontend**: HTML templates
- **Version Control**: Git + GitHub

---

## ✅ Project Status
**Fully Functional** ✅
- Home page at `/` renders successfully
- Admin panel at `/admin/` working with Student and Profile models
- CRUD operations working on both models
- All migrations applied cleanly

