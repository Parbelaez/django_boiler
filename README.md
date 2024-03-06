# django_boiler
 boilerplate for Django Projects

 1. Create a virtual environment:
    ```
    python3 -m venv .venv
    ```
2. Activate the virtual environment:
    ```
    source .venv/bin/activate
    ```
3. Install django:
    ```
    pip install django
    ```

4. Create a new project:
    ```
    django-admin startproject project_name .
    ```
*Note: The dot at the end of the command is important. It tells Django to create the project in the current directory.*

*IMPORTANT:* to use this boilerplate, you need to delete the test_django folder and the manage.py file before running the startproject command.

5. Test the project:
    ```
    python manage.py runserver
    ```

6. Open the browser and go to http://127.0.0.1/8000

You should see the Django welcome page.

![Django Welcome Page](.readme_images/django_welcome_page.png)

7. Create a env.py file and add the following:
    ```
    import os

    os.environ['DATABASE_URL'] = 'your_database_url'
    os.environ['SECRET_KEY'] = 'your_secret_key'
    os.environ['DEBUG'] = 'True'
    os.environ['CLOUDINARY_URL'] = 'your_cloudinary_url'
    ```
*Note: The env.py file should not be committed to the repository.*

8. Add the environment variables file to the settings.py file:
    ```
   if os.path.exists('env.py'):
       import env
    ```

9. Install the following packages:
    ```
    pip install dj_database_url
    pip install psycopg
    ````
The dj_database_url package allows you to use the DATABASE_URL environment variable to configure the database.
The psycopg package is a PostgreSQL adapter for Python.

10. Add the following to the settings.py file:
    ```
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config()
    }
    ```
*Note: This will allow you to use the DATABASE_URL environment variable to configure the database.*

In this case, the production DB will be used right from the begining to confirm that everything is working as expected.

11. Change the secret key to use the environment variable:
    ```
    SECRET_KEY = os.environ['SECRET_KEY']
    ```

12. Add the following to the settings.py file:
    ```
    DEBUG = os.environ['DEBUG']
    ```
*Note: This will allow you to use the DEBUG environment variable to configure the debug mode.*

13. Change the allowed hosts so the app can run locally and on Heroku (or the cloud provider of your choice):
    ```
    ALLOWED_HOSTS = ['127.0.0.1/8000', 'localhost', '.herokuapp.com']
    ```

14. Migrate the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
*Note: This will create the database tables.*
In this case, the makemiogrations command is not necessary because we do not have any models or custom schemas, just the expected django ones.

15. Create a superuser:
    ```
    python manage.py createsuperuser
    ```
*Note: This will allow you to access the admin panel.*

16. Test the project:
    ```
    python manage.py runserver
    ```
Open the browser and go to http://127.0.01/8000/admin

You should see the Django admin login page.

![Django Admin Login Page](.readme_images/django_admin_login_page.png)

Enter the superuser credentials and you should see the Django admin panel.

![Django Admin Panel](.readme_images/django_admin_panel.png)


    
