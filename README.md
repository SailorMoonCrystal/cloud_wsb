## Opis

This project is used for storing information about houseplants, with all basic CRUD operations for database implemented.

## Deployment

1. Python 3.9
1. ./setup.py install

## Development
To run the app you need Python 3.9(or newer).

1. Create virtualenv
2. pip install -r requirements.txt
2a. [OPTIONAL] Install extra binaries if encountered any issues with cairo/pandas packages (os dependent)
2b. pip install -r requirements_dev.txt
2c. pre-commit install
3. npm install
4. npm start
5. python manage.py migrate
6. python manage.py populatedb
7. python manage.py runserver

Your server should be available at http://127.0.0.1:8000

## Environment variables
### Application
- `SECRET_KEY` - `str` - defaults to `secret` (unused)
- `DATABASE_URL` - `str` - defaults to `project.sqlite3` in the root project path.
- `DEBUG` - `bool` - `True` for development, `False` for production (default).
- `ALLOWED_HOSTS` - `list` - Allowed hosts to connect from, `127.0.0.1,localhost` by default. Separate each entry using a comma.