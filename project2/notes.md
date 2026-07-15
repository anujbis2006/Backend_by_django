# Project 2 Notes

This project is a Django web app focused on learning URL routing, views, and request handling in a small `blog` app.

## Project Structure

- `manage.py` is the main command-line entry point for the project.
- `project2/` contains the project configuration:
  - `settings.py`
  - `urls.py`
  - `asgi.py`
  - `wsgi.py`
- `blog/` contains the app logic for the blog routes and views.
- `db.sqlite3` is the local SQLite database used by the project.

## What I Learned So Far

- Django management commands matter a lot. `python3 manage.py runserver` starts the development server, but `startserver` is not a valid Django command.
- URL routing is controlled in two places:
  - the project-level `project2/urls.py`
  - the app-level `blog/urls.py`
- `include('blog.urls')` connects the blog app routes to the main project under the `/blog/` prefix.
- A small regex typo in `re_path()` can break the whole site. I fixed `(?p<year>...)` to `(?P<year>...)`.
- Route structure must match the URL I actually visit in the browser. The app needed a direct date route for `/blog/2024/1/12/`.

## URL Routes I Have Built

- `/admin/` opens the Django admin site.
- `/blog/post/<post_id>/` shows a post detail page.
- `/blog/user/<username>/` shows a user profile page.
- `/blog/<year>/<month>/<day>/` shows an article by date.
- `/blog/article/<year>/<month>/` shows an article by year and month.
- `/blog/article/<year>/` is also supported with `re_path()`.

## Views

- `post_details(request, post_id)` returns a simple HTML response with the post ID.
- `user_provide(request, username)` returns a simple HTML response with the username.
- `article_by_year(request, **kwargs)` currently accepts route values through `kwargs` and returns them in the response.

## Important Fixes Made

- Replaced the invalid regex group syntax in `blog/urls.py`.
- Added a direct year/month/day route so the URL used in the browser resolves correctly.
- Verified the project with `python3 manage.py check`, and Django reported no issues.

## Commands I Used

- `python3 manage.py check`
- `python3 manage.py runserver`

## Next Things To Improve

- Make the `article_by_year` response format cleaner.
- Add more blog pages and maybe templates instead of raw `HttpResponse` output.
- Add tests for the URL patterns and view responses.