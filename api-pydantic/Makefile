default: web

web:
	poetry run flask --app apipydantic run --debug

test:
	poetry run ruff --fix apipydantic
	poetry run mypy apipydantic
