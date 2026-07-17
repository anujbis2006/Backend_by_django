# Project 8 Notes

This project is a Django practice app focused on template inheritance, static files, URL routing, and building a small site with multiple pages.

## Project Structure

- `manage.py` runs the Django project.
- `project8/` contains the main project configuration and root URL routing.
- `blog/` contains the app views and app-specific URLs.
- `templates/` contains shared templates like `base.html` and `navbar.html`.
- `templates/home.html` is the home page template.
- `blog/templates/blog/about.html` is the about page template.
- `static/css/style.css` contains styling.
- `static/js/script.js` contains JavaScript behavior.
- `db.sqlite3` is the SQLite database.

## What I Learned

### 1. Template Inheritance Keeps Pages Consistent

I learned how to use `{% extends %}` and `{% block %}` to build pages on top of a shared layout.

`base.html` provides the common structure for the site, and `home.html` and `about.html` fill in the page-specific content.

### 2. Shared Layouts Reduce Repetition

The `base.html` file includes:

- the HTML skeleton
- a shared title block
- the navbar include
- the footer
- links to CSS and JavaScript files

This makes the project easier to manage because the same layout is reused on multiple pages.

### 3. URL Routing Must Match the View Functions

I learned how the root project URL file includes the blog app routes.

The app URL file maps:

- `/` to `home()`
- `/about/` to `about()`

This showed me how `include()` and `path()` work together to make the site accessible.

### 4. Template Paths Must Match Render Calls

In `views.py`, the `home()` view renders `home.html` and the `about()` view renders `blog/about.html`.

I learned that the render path must match the actual template location, or Django will fail to find the file.

### 5. Static Files Need Proper Setup

The project uses the `static` template tag for the logo image and loads CSS and JavaScript from the `static/` folder.

I learned that:

- `{% load static %}` must be added in templates that use static files
- `STATICFILES_DIRS` must point to the static folder
- file paths in `static` tags must be written carefully

### 6. Forms Need Correct HTML and CSRF Protection

The home page includes a POST form with a CSRF token.

That taught me that Django forms should include:

- `method="post"`
- `{% csrf_token %}`
- proper input names

### 7. Small Template Syntax Mistakes Can Break the Page

I ran into errors from malformed template syntax, such as broken `{% extends %}` and `{% block %}` tags.

I learned that Django template syntax is strict, and even a small typo can prevent the page from rendering.

### 8. Navbar Links Depend on Named Routes

The navbar uses `{% url 'home' %}` and `{% url 'about' %}`.

This taught me that named routes are a clean way to keep links working even if the URL path changes later.

## Fixes I Made

### Broken Home Template Syntax

I corrected the `home.html` template so it properly extends `base.html`, loads static files, and uses valid block syntax.

### Missing About Page

I added `blog/templates/blog/about.html` because the navbar already linked to the about route.

### Root URL Wiring

I confirmed the project root URL file includes the blog app so `/` works correctly.

### Static and Shared Template Setup

I verified the project has a shared `base.html`, a reusable `navbar.html`, CSS, and JavaScript files so the site can grow cleanly.

## Important Files

- `project8/project8/urls.py`
- `project8/blog/urls.py`
- `project8/blog/views.py`
- `project8/templates/base.html`
- `project8/templates/navbar.html`
- `project8/templates/home.html`
- `project8/blog/templates/blog/about.html`
- `project8/static/css/style.css`
- `project8/static/js/script.js`

## Current Working Pages

- `/` opens the home page.
- `/about/` opens the about page.

## What I Would Improve Next

- Add real form handling for the login form.
- Make the JavaScript button do something useful.
- Improve the layout and styling of the home page.
- Add more pages and reusable template sections.
