# Modern Flask Application

## Development

```
pip install -r requirements.txt -r requirements-dev.txt
flask run
flask job user_count
```

## Production

```
waitress-serve --port=5000 --call modern:create_app
```
