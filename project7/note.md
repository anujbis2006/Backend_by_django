# Project 7 Notes

This project is a Django practice app focused on template rendering, context data, URL routing, and fixing common template syntax mistakes.

## Project Structure

- `manage.py` runs Django commands.
- `project7/` contains the main project settings and URL configuration.
- `blog/` contains the app logic, views, URLs, and templates.
- `blog/templates/blog/blog_list.html` is the main template for the page.
- `db.sqlite3` is the SQLite database.

## What This Project Is About

The goal of project 7 was to render a blog list page and practice showing data from a Django view inside a template.

The page uses:

- lists of dictionaries
- booleans
- strings
- the current date/time
- safe HTML output
- template tags like `if`, `for`, `with`, `firstof`, `verbatim`, and `autoescape`

## What I Learned

### 1. View and Template Context Must Match

In `blog/views.py`, the view sends a context dictionary to the template.

I learned that the variable names in the view must match what the template expects.

For example:

- the view sends `blogs`
- the template loops over `blogs`
- if the names do not match, the page will render incorrectly or look empty

### 2. Django `with` Tag Syntax Is Strict

I hit a `TemplateSyntaxError` because the `with` tag was written with spaces around `=`.

The correct format is:

- `{% with total_blogs=blogs|length %}`

I learned that Django template syntax is picky, and small spacing mistakes can break the page.

### 3. Root URL Routing Controls What Opens in the Browser

The project root URL points to the blog app using `include('blog.urls')`.

That taught me that the browser path `/` only works if the root URL configuration sends requests to the correct app.

### 4. Templates Can Display Different Kinds of Data

The page shows how Django templates can handle:

- list looping with `{% for %}`
- conditionals with `{% if %}`
- fallback values with `{% firstof %}`
- raw template text with `{% verbatim %}`
- HTML escaping and trusted output with `safe` and `autoescape`

### 5. HTML Output Should Be Controlled Carefully

The view passes `html_code` as a string containing HTML.

I learned that Django escapes HTML by default, and only trusted content should be rendered with `|safe` or inside `autoescape off`.

### 6. Running Commands From the Correct Folder Matters

At one point, `runserver` failed because it was started from the wrong directory.

I learned that Django commands should be run from the folder that contains `manage.py`.

## Errors I Fixed

### Context Name Mismatch

The template expected `blogs`, but the view originally sent `blog`.

I fixed that by renaming the context key to `blogs`.

### Malformed `with` Tag

The template used an invalid `with` expression.

I corrected the syntax so Django could parse the template.

### Wrong Working Directory

The server command failed when it was run from the repo root instead of `project7`.

Running `python3 manage.py check` from the correct directory confirmed the project configuration is valid.

## Current Working Route

- `/` opens the blog list page.

## Important Files

- `project7/project7/urls.py`
- `project7/blog/urls.py`
- `project7/blog/views.py`
- `project7/blog/templates/blog/blog_list.html`

## What I Would Improve Next

- Add a base template for shared layout.
- Split the template examples into smaller pages.
- Replace hardcoded blog data with database models.
- Add CSS so the page looks cleaner.
