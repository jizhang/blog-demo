default: web

web:
	poetry run flask run --debug

test:
	poetry run ruff --fix apipydantic
	poetry run mypy apipydantic
