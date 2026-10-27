# Steps to create a Django Project

1. Create a folder for the new project
2. Open VS Code and a terminal at that project (or any other IDE)
3. Create the virtualenvironment  
    - Mac: python3 -m venv venv (Last parameter is optional, not mandatory to call it 'venv')
    - Windows: python -m venv venv  
4. Activate the venv  
    - Mac: source venv/bin/activate
    - Windows: .\venv\Scripts\activate  
5. Install the required dependencies  
    - Both OS: pip install django (pip3 if you're on a MAC)  
6. Create the django project (One time only command)
    - Both OS: django-admin startproject NAME_FOLDER .
    Expectation is: NAME_FOLDER folder, venv folder and manage.py
7. Update settings.py to recognize **static** and **templates** folders
    Expectation is: templates and static folders are created  
    7.1. Inside of static you can create three subfolders called: js, images and css
8. Adding misc files: .gitignore, README.md
9. To generate the requirements.txt file:
    - Both OS: pip freeze > requirements.txt (pip3 if you're on a MAC)

## Django Subcommands
1. To create a django app:

    - Both OS: python manage.py startapp APP_NAME (python3 if you're on a MAC)

2. To verify if we have issues/errors:

    - Both OS: python manage.py check

3. To create an admin user:

    - Both OS: python manage.py createsuperuser
    - This will ask you for a username, email, password and password confirmation

4. To detect changes and create migrations files (MODELS):

    - Both OS: python manage.py makemigrations

5. To execute changes against the db:

    - Both OS: python manage.py migrate

6. To run the server:

    - Both OS: python manage.py runserver

## Class 1 – Assignment 1

### About Me page

The About Me assignment is available at `/about/` and includes:

- `AboutPageView` inside the `pages` app.
- An About Me template with a personal introduction.
- A URL pattern connected to the About page.
- A page-specific stylesheet with responsive interest cards.

### Verify the assignment

From the project folder, run:

```text
python manage.py check
python manage.py runserver
```

Then open `http://127.0.0.1:8000/about/` in a browser.

Repository: https://github.com/git-oojl/FSDI-112

## Class 2 – Assignment 2

### Templates using Django Template Language and static files

The About Me page was updated to use the shared template structure:

- `about.html` extends `base.html`.
- `base.html` includes the shared navbar from `navbar.html`.
- The About page loads its page-specific stylesheet with `{% load static %}`.
- The page is available at `/about/`.

### Verify the assignment

Run the project and open `http://127.0.0.1:8000/about/` to verify the inherited navbar, About Me content, and styling.

Repository: https://github.com/git-oojl/FSDI-112

## Class 3 – Assignment 3

### Blog App: Post model

The Blog App data was created through the Django Administration site at `/admin/`:

- 2 additional users were added: `graphics_dev` and `backend_builder`.
- 5 Post records were created and assigned across the available users.
- The posts are visible at `/posts/list/`.

Repository: https://github.com/git-oojl/FSDI-112
