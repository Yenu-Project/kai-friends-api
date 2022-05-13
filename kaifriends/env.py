import environ
from os import environ as os_environ

env = environ.Env(
    KAIFRIENDS_DB_NAME=(str, os_environ.get('KAIFRIENDS_DB_NAME')),
    KAIFRIENDS_DB_USER=(str, os_environ.get('KAIFRIENDS_DB_USER')),
    KAIFRIENDS_DB_PASSWORD=(str, os_environ.get('KAIFRIENDS_DB_PASSWORD')),
    KAIFRIENDS_DB_HOST=(str, os_environ.get('KAIFRIENDS_DB_HOST')),
    KAIFRIENDS_DB_PORT=(str, os_environ.get('KAIFRIENDS_DB_PORT')),
    SECRET_KEY=(str, os_environ.get('SECRET_KEY'))
)
