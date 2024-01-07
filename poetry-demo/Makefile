default: web

web:
	FLASK_APP=poetrydemo poetry run flask run

dev:
	poetry install

prod:
	poetry install --without dev --extras gunicorn
