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

![Django Welcome Page](./readme_images/django_welcome_page.png)

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
    import os

    ...

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
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL")),
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

![Django Admin Login Page](./readme_images/django_admin_login_page.png)

Enter the superuser credentials and you should see the Django admin panel.

![Django Admin Panel](./readme_images/django_admin_panel.png)

17. Create a requirements.txt file:
    ```
    pip freeze > requirements.txt
    ```

18. Create a Procfile file:
    ```
    echo web: gunicorn project_name.wsgi:application > Procfile
    ```

19. Install the following packages:
    ```
    pip install gunicorn
    pip install cloudinary
    ```
The gunicorn package is a Python WSGI HTTP Server for UNIX. Basically what it does is to create a server that can handle the requests from the web and send them to the Django app.

Cloudinary is a cloud-based image and video management service. The cloudinary package is a package that facilitates Django's usage of the files saved in this cloud service.

*Note: The cloudinary package is not necessary for the project to work, but it is a good practice to use a cloud service to store the files. If you would like to use a different one, then please read the documentation for that specific cloud and proceed as indicated there, not in this document.*

20. Add the following to the settings.py file:
    ```
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api

    CLOUDINARY_URL = os.environ['CLOUDINARY_URL']
    cloudinary.config(
        cloud_name=os.environ['CLOUDINARY_CLOUD_NAME'],
        api_key=os.environ['CLOUDINARY_API_KEY'],
        api_secret=os.environ['CLOUDINARY_API_SECRET']
    )
    ```
*Note: This will allow you to use the CLOUDINARY_URL environment variable to configure the cloudinary service.*

---
Until here, the project is ready to be deployed to Heroku. The next steps are to create a Heroku app and deploy the project to it.
Also, to create apps inside this boiler plate, please refer to my previous Django projects.
---

From here on, we will continue creating an API for the project by using the Django REST framework.

21. Install the following packages:
    ```
    pip install djangorestframework
    pip install django-cors-headers
    ```
The djangorestframework package is a powerful and flexible toolkit for building Web APIs.
The django-cors-headers package is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

22. Add the following to the settings.py file:
    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'corsheaders',
    ]
    ```

23. Add the following to the settings.py file:
    ```
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        ...
    ]
    ```
*Note: This will allow the server to handle the server headers required for Cross-Origin Resource Sharing (CORS).*

IMPORTANT: The order of the middleware is important. The CorsMiddleware should be placed as high as possible, especially before any middleware that can generate responses such as Django's CommonMiddleware or Whitenoise's WhiteNoiseMiddleware.

24. Add the following to the settings.py file:
    ```
    CORS_ORIGIN_ALLOW_ALL = True
    ```
*Note: This will allow the server to accept requests from any origin.*

25. Create a home view (optional)

You must create a views.py file in the porject folder:

    ```
    touch ./project_name/views.py
    ```
Add the following to the views.py file:
    ```
    from rest_framework.decorators import api_view
    from rest_framework.response import Response


    @api_view()
    def root_route(request):
        return Response({
            your message here
        })
    ```
With this view, you can test the API by going to http://127.0.0.1/8000/

![Django API](./readme_images/django_api.png)

26. Setup the authentication

As DRF comes with a default authentication system, you can use it out of the box.

Add the following to the settings.py file:
    ```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
    }
    ```
 and add the url to the urls.py file:

    ```
    from django.urls import path, include

    ...
    path('api-auth/', include('rest_framework.urls')),
    ```

Now you should have the authentication system working, and it can be seen in the browsable API, with the login and logout options.

![Django Browsable API Auth](./readme_images/django_browsable_api_auth.png)

*OPTIONAL: JWT Authentication*

If you want to use JWT authentication, you can install the following package:
    ```
    pip install dj-rest-auth
    pip install djangorestframework_simplejwt
    ```

Add the app to the INSTALLED_APPS list in the settings.py file:
    ```
    INSTALLED_APPS = (
        ...,
        'rest_framework',
        'rest_framework.authtoken',
        ...,
        'dj_rest_auth'
    )
    ```

Add the urls to the urls.py file:
    ```
    ...
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
    ```

Migrate the database:
    ```
    python manage.py migrate
    ```

*ADVANCED AUTHENTICATION*

If you want to use a more advanced authentication system, you can install the following package:
    ```
    pip install django-allauth
    ```
Django Allauth is a flexible authentication app that can be used to add social authentication to the project.
Also, it can be used to add email confirmation, password reset, and other features.

More info at: https://docs.allauth.org/en/latest/introduction/index.html

Add the app to the INSTALLED_APPS list in the settings.py file:
    ```
    INSTALLED_APPS = (
        ...,
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        ...
    )
    ```
