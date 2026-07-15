# Project 3 Notes

This project is a simple Django app built to understand basic URL routing, template rendering, and the connection between a view and an HTML file.

## Project Structure

- `manage.py` is the command-line entry point for the project.
- `project3/` contains the project configuration:
  - `settings.py`
  - `urls.py`
  - `asgi.py`
  - `wsgi.py`
- `templates/` contains the HTML templates used by the project.
- `db.sqlite3` is the local SQLite database.

## What I Learned So Far

- A Django project can render a template instead of returning raw HTML from a view.
- The `home()` view in `project3/views.py` uses `render(request, 'home.html')`.
- The `TEMPLATES` setting in `settings.py` must point to the correct `templates` folder for Django to find `home.html`.
- `ROOT_URLCONF = 'project3.urls'` connects the main URL configuration for the project.
- The root route `''` is mapped to the home page, so visiting the site opens the template-rendered homepage.
- `path('admin/', admin.site.urls)` enables the Django admin site.

## URL Routes

- `/` opens the home page.
- `/admin/` opens the Django admin site.

## View and Template Flow

- `project3/views.py` defines a simple `home(request)` view.
- That view renders `home.html` from the `templates/` directory.
- `templates/home.html` currently shows a simple `Hello World!` message and a short paragraph.

## Important Settings

- `DEBUG = True` is enabled for development.
- `ALLOWED_HOSTS = []` is currently empty.
- `DIRS` inside `TEMPLATES` includes the project-level `templates` folder.
- `DATABASES` is configured to use SQLite.

## Current Learning Takeaways

- URL configuration and view rendering are closely connected.
- A project-level template folder is an easy way to keep HTML separate from Python code.
- Even a small project helps show how Django resolves a request from URL to view to template.

## Next Things To Improve

- Add more pages and routes beyond the home page.
- Replace the placeholder HTML with a more styled homepage.
- Add app-specific views and templates to practice multiple pages.