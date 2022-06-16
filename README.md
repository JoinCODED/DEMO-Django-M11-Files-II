# Django Files II

Show students file management in templates

## What are the objectives?

- Understand how to use static files to manage their stylesheets and AJAX
- Understand how to use media files in templates

## Pre-requisites

1. Clone this repo.
2. Create a virtual environment.
3. Install the deps using `pip install -r requirements/dev.lock`.
4. Create an admin account using `python manage.py createsuperuser`.

## Steps

### Static & Media Files

1. Add the set up for static files in `settings.py`:

   ```python
   STATIC_URL = "static/"
   STATIC_ROOT = BASE_DIR / "static"
   ```

2. Add the set up for static files in `urls.py`:

   ```python
   ...

   from django.conf import settings
   from django.conf.urls.static import static


   urlpatterns = [
       ...
   ]

   if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   ```

3. Add the set up for media files in `settings.py`:

   ```python
   MEDIA_URL = "media/"
   MEDIA_ROOT = BASE_DIR / "media"
   ```

4. Add the set up for media files in `urls.py`:

   ```python
   ...


   urlpatterns = [
       ...
   ]

   if settings.DEBUG:
       ...
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

5. Go the admin site and create some ships (if you do this step before setting up media files, the images will be in the root directory of the project).
6. Go to `http://localhost:8000/ships/` and show them the current template.
7. Add a `static` folder inside of `ships`, and explain that you will be adding your images/stylesheets here.
8. Add a stylesheet, call it `ship_list.css` inside of `ships/static`.
9. Link the stylesheet using the following:

   ```html
   <!DOCTYPE html>
   {% load static %}
   <html lang="en">
     <head>
       ...
       <link rel="stylesheet" href="{% static 'ship_list.css' %}" />
     </head>
     ...
   </html>
   ```

10. Add the following css:

    ```css
    body {
      background-color: salmon;
      font: 1rem arial, san-serif;
    }

    ul {
      padding: 0;
      margin: 1em 0;
    }

    li {
      list-style: none;
    }

    hr {
      display: none;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(17rem, 1fr));
      gap: 1em;
    }

    .card {
      display: grid;
      place-items: center;

      background-color: #fff;
      border-radius: 8px;
      padding: 1em;
    }

    .card-img {
      height: 7.5rem;
      width: 7.5rem;
      object-fit: contain;
    }
    ```

11. Refresh the page and show them that their site is now pretty!
12. The images are still broken though 🙁, so time to fix that as well.
13. Go ahead and add the `src` for the ship's banner like so:

    ```html
    <img class="card-img" src="{{ ship.banner }}" alt="{{ ship.model }}" />
    ```

14. Refresh the page, and it still does not work!
15. Show them that they need to access the url attribute like so:

    ```html
    <img class="card-img" src="{{ ship.banner.url }}" alt="{{ ship.model }}" />
    ```

### Media Files w/ Forms

1. Go to `http://localhost:8000/ships/create`, and show them our `crispy` form.
   - Right now, we are only rendering the form, we need to actually handle media files
2. Update our template's `form` tag like so:

   ```html
   <form
     action="{% url 'create-ship' %}"
     method="POST"
     enctype="multipart/form-data"
   >
     ...
   </form>
   ```

   - Explain that `enctype` is what will allow us to deal with user-uploaded files

3. Update our view so that we are handling the file upload:

   ```python
   def create_ship(request: HttpRequest) -> HttpResponse:
       form = ShipForm()
       if request.method == "POST":
           form = ShipForm(request.POST, request.FILES)
           if form.is_valid():
               form.save()
               return redirect("ship-list")
       context = {
           "form": form,
       }
       return render(request, "create_ship.html", context)
   ```

   - When the view is receiving a form submission and that form has file, to receive the files submitted with that form we have to include `request.FILES` as well.

4. Test out the form now and show them that it works.
