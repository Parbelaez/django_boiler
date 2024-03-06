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

5. Test the project:
    ```
    python manage.py runserver
    ```

6. Open the browser and go to http://127.0.0.1/8000

You should see the Django welcome page.

[Django Welcome Page](.readme_images/django_welcome_page.png)

4. Create a .env file and add the following:
    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```
5. Run the server:
    ```
    python manage.py runserver
    ```
6. Open the browser and go to http://

