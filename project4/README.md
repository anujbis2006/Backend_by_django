# Project 4

This project is a Django app built to practice reusable templates, shared layout structure, and separate app pages for blog and shop content.

## What I Did First

I started by creating the Django project structure and then added two apps:

- `blog`
- `shop`

After that, I connected both apps in the main project URL configuration so their pages could be reached through the browser.

## Main Project Setup

- `manage.py` is the entry point for running the project.
- `project4/` contains the project settings, URL config, ASGI, and WSGI files.
- `blog/` holds the blog page logic.
- `shop/` holds the shop page logic.
- `templates/` contains the shared base template used by both apps.

## What I Changed

- I set up a shared base template in the project-level `templates` directory.
- I made the blog and shop templates extend that base template.
- I updated the project settings so Django can find the shared template folder.
- I linked the blog and shop apps into the main URL routes.
- I fixed template syntax issues in the base file so Django block inheritance works properly.
- I corrected the template lookup so the blog and shop views render the right HTML files.

## How the Pages Work

- The blog page loads through the blog app view and inherits the shared layout.
- The shop page loads through the shop app view and also inherits the shared layout.
- The base template provides the common structure, while each app template fills in its own title and content.

## What I Learned

- Shared templates make it easier to keep the site layout consistent.
- Django template inheritance lets one base file control the page shell.
- App templates can reuse the same layout without copying the full HTML each time.
- Small template tag mistakes can break the whole page, so syntax matters.
- Django settings must point to the correct template directory or the pages will not render.

## Current Pages

- `/blog/` shows the blog page.
- `/shop/` shows the shop page.
- `/admin/` opens the Django admin site.

## Verification

- I checked the templates after fixing the base file and Django accepted them.
- The project now loads the shared base template correctly for the blog and shop pages.
