# Project 5 Notes

This project is a Django practice app focused on learning template rendering, context data, dot-notation access in templates, and fixing common routing/template mistakes.

## How I Started

I began by creating the Django project and then adding a `blog` app.

The main goal was to build one home page that could display different kinds of data coming from the view:

- strings
- numbers
- lists
- custom Python objects
- nested dictionaries
- HTML content

## Project Structure

- `manage.py` is used to run Django commands.
- `project5/` contains the project configuration.
- `blog/` contains the app logic, URL routing, and templates.
- `blog/templates/blog/home.html` is the page template for the home view.
- `db.sqlite3` is the SQLite database.

## Main Things I Learned

### 1. Views Can Send Context Data

In `blog/views.py`, the `home()` view builds a context dictionary and sends it to the template.

That context includes:

- `name`
- `age`
- `skill`
- `user`
- `blog`
- `empty`

This showed me how Django can pass data from Python into HTML.

### 2. Custom Objects Can Be Used in Templates

I created a small `user` class in the view file and passed an instance of it into the template.

That helped me learn how template dot notation works, such as:

- `{{ user.name }}`
- `{{ user.age }}`

### 3. Nested Dictionaries Work Well in Templates

The `blog` dictionary contains nested data like:

- `blog.title`
- `blog.author.name`
- `blog.created_at`
- `blog.content`

This made it clear that Django templates can read nested dictionary values using dot notation.

### 4. HTML Can Be Rendered Safely Only When Needed

The blog content includes HTML tags, so I used the `safe` filter in the template for that field.

That taught me that Django escapes HTML by default, and only trusted content should be marked safe.

### 5. Default Values Are Useful

I used the `default` filter for `empty`.

That showed me how to display a fallback value when data is missing or blank.

### 6. URL Routing Must Match the View

The blog app URL file maps the empty route `''` to `views.home`.

The main project URL file includes the blog app and also exposes it at the root path.

This helped me understand how `include()` and `path()` work together.

## Template Learning Summary

The `home.html` file taught me how to:

- print simple variables
- print lists and object fields
- show nested dictionary values
- use template filters
- keep HTML structure separate from Python logic

## Important Fixes I Made

### Home View Scope Problem

At one point, `home()` was nested inside the `user` class, which caused Django to fail when importing the view.

I fixed that by moving `home()` to the module level.

### Template Path Problem

The template file lives at `blog/templates/blog/home.html`, so the render call had to use `blog/home.html`.

### Root URL Problem

The browser was opening `/`, but only `/blog/` was connected.

I fixed that by adding the blog include to the root URL configuration.

## Current Working Pages

- `/` opens the blog home page.
- `/blog/` also opens the same blog home page.

## What I Understand Better Now

- How context data moves from a view into a template.
- How Django template dot notation works.
- How to organize app templates inside an app-specific templates folder.
- How small syntax and scope mistakes can break a Django project.
- How URL configuration controls what the browser can reach.

## Next Things I Could Improve

- Add more pages for the blog app.
- Split the data into separate templates or views.
- Make the home page look better with CSS.
- Add a base template if I want multiple pages to share the same layout.
