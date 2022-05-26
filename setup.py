from setuptools import setup, find_packages

setup(
    name='modern',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'modern=modern:cli'
        ],
    },
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy'
    ],
    setup_requires=[],
    tests_require=[
        'pytest'
    ]
)
