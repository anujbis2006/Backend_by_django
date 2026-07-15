# Project 4 Notes

This note file tracks what I learned and changed while building project 4.

## Starting Point

I created a new Django project and added two apps for separate parts of the site:

- `blog`
- `shop`

The first goal was to get both apps connected to the main project and load a page from each one.

## Project Structure

- `manage.py` runs the project commands.
- `project4/` contains the project configuration files.
- `blog/` contains the blog view and URL setup.
- `shop/` contains the shop view and URL setup.
- `templates/` contains the shared base layout.

## Template Flow

- The shared layout lives in `templates/base.html`.
- The blog page template extends the base template.
- The shop page template also extends the base template.
- This means the header, shared structure, and page wrapper live in one place.

## Changes I Made

- I added the shared base template at the project level instead of repeating layout in each app.
- I configured the template directory in Django settings.
- I connected blog and shop routes through the project URL file.
- I updated the views so they render the app templates directly.
- I fixed the Django block tag syntax in the base template.
- I corrected the template names so the app pages resolve properly.

## Mistakes I Fixed

- I had incorrect template block syntax in `base.html`.
- I had a project-name typo in the Django bootstrap files earlier.
- I had template path mismatches before switching the views to the shared app templates.

## Final Learning

- Template inheritance is the cleanest way to share layout in Django.
- The base template controls the shared look and feel.
- Blog and shop pages can keep their own content while using the same layout.
- Django settings, views, and templates all have to agree on the same folder names.

## Files That Matter Most

- `project4/settings.py`
- `project4/urls.py`
- `templates/base.html`
- `blog/views.py`
- `blog/templates/post_list.html`
- `shop/views.py`
- `shop/templates/shop_list.html`
