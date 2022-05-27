from setuptools import setup, find_packages

setup(
    name='nasa',
    packages=find_packages(),
    install_requires=[
        'Flask>=2',
        'SQLAlchemy>=1.4,<2',
        'PyMySQL',
        'python-dotenv',
    ]
)
