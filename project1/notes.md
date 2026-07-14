# Project 1 Notes

This project is a Django 6.0.7 web app with two local apps: `blog` and `shop`.

## Main Structure

- `manage.py` starts and manages the Django project.
- `project1/` contains the project configuration:
  - `settings.py`
  - `urls.py`
  - `asgi.py`
  - `wsgi.py`
- `blog/` is the blog app.
- `shop/` is the shop app.
- `db.sqlite3` is the local SQLite database.

## URL Routes

- `/admin/` goes to the Django admin site.
- `/blog/` includes the blog app routes.
- `/shop/` includes the shop app routes.

## Blog App

- `blog/views.py` has two simple views:
  - `home()` returns: `Hello, welcome to the blog!`
  - `about()` returns: `Hello, welcome to the about page!`
- `blog/urls.py` maps:
  - `/blog/` to the blog home page
  - `/blog/about/` to the about page

## Shop App

- `shop/views.py` has two simple views:
  - `home()` returns: `Hello, welcome to the shop!`
  - `products()` returns: `Hello, welcome to the products page!`
- `shop/urls.py` maps:
  - `/shop/` to the shop home page
  - `/shop/products/` to the products page

## Settings

- `blog` and `shop` are added to `INSTALLED_APPS`.
- The project uses SQLite as the default database.
- `DEBUG = True` is enabled for development.

## Current Notes

- The project has been verified with `python manage.py check`.
- The home and about routes respond correctly in the browser.
- The old `README.md` was removed and replaced with this notes file.