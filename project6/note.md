# Project 6 Notes

This project is a Django learning project built to understand template filters, template rendering, context handling, and how small mistakes in a view or template can break a page.

## What This Project Is About

The main goal of project 6 was to build a blog detail page and practice showing different kinds of data in a Django template.

Instead of only printing plain text, this project uses:

- strings
- numbers
- dates and times
- lists
- `None` values
- HTML-safe content
- built-in Django template filters

## Project Structure

- `manage.py` runs the Django project.
- `project6/` contains the main project settings and URL routing.
- `blog/` contains the blog app.
- `blog/views.py` builds the context data for the page.
- `blog/urls.py` connects the blog route to the view.
- `blog/templates/blog/blog_detail.html` contains the page template.
- `db.sqlite3` is the SQLite database.

## How the Page Works

The request flow is:

1. The browser opens the site.
2. Django checks the project URL configuration.
3. The root path is routed into the blog app.
4. The blog app URL file sends the request to `blog_detail()`.
5. The view creates a `post` dictionary and passes it to the template.
6. The template reads the values and displays them using Django filters.

This helped me understand how Django connects URLs, views, and templates together.

## What I Learned

### 1. Views Can Build Rich Context Data

In `blog/views.py`, I created a dictionary named `post`.

That dictionary stores:

- title
- description
- author
- created time
- comment count
- tags
- price

This showed me how a single view can prepare many kinds of values for the template.

### 2. Template Filters Make Display Cleaner

The blog detail template uses several built-in Django filters.

I learned how to use filters like:

- `default`
- `pluralize`
- `date`
- `time`
- `urlencode`
- `floatformat`
- `upper`
- `lower`
- `capfirst`
- `title`
- `truncatechars`
- `truncatewords`
- `linebreaks`
- `add`
- `divisibleby`
- `last`
- `length`
- `slice`
- `join`

These filters help format data directly inside the template without writing extra Python logic.

### 3. `None` Values Need Safe Handling

The `author` field is set to `None`.

I learned that templates can show a fallback value with the `default` filter, which is useful when the data may be missing.

### 4. Dates and Times Need Special Formatting

The project uses a `datetime` value in the view.

The template formats that value using:

- `date:"d/m/Y"`
- `time:'H:i'`

That taught me how Django can display dates in a custom readable format.

### 5. Lists Can Be Printed and Manipulated in Templates

The `tags` field is a list.

The template shows how to:

- get the last item
- count the number of tags
- slice the list
- join the list into a sentence

This is useful when you want to show structured data on a page.

### 6. Numbers Can Be Used in Template Logic

I used `divisibleby` to check if a number is even or odd.

That helped me understand that templates can also include simple logic, not just display text.

## Mistakes I Fixed

### Invalid Filter Syntax

At first, the template had invalid filter syntax like a broken `author` expression and incorrect filter names.

I corrected those so Django could parse the template.

### Missing Context Value

The template tried to use a variable named `number`, but the view did not pass it.

That caused a `TypeError` during rendering because `divisibleby` received `None`.

I fixed it by adding a numeric value in the context.

### View and Template Coordination

I learned that the view and template must agree on the same variable names.

If the template expects `number`, the view must provide `number`.

If the template expects `post.comment_count`, the dictionary must contain `comment_count`, not a different key name.

## Important Learning Outcomes

- Django templates can format data in a very readable way.
- Context data should be named carefully so the template can access it correctly.
- Small typos in template filters can break the whole page.
- A missing value in the context can cause a runtime error even when the project structure is correct.
- Running `manage.py check` is useful, but direct rendering is often better for catching template runtime issues.

## Final Working Route

- `/` opens the blog detail page.

## Files That Matter Most

- `project6/project6/urls.py`
- `project6/blog/urls.py`
- `project6/blog/views.py`
- `project6/blog/templates/blog/blog_detail.html`

## What I Would Improve Next

- Add a base template so multiple pages can share the same layout.
- Split the blog detail example into smaller pages.
- Add more routes for different posts.
- Make the page style cleaner with CSS.
