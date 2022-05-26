from flask import current_app


@current_app.cli.command('user_count')
def run():
    print(1)
