from os import environ

class Config:
    SECRET_KEY = \
        environ.get('SECRET_KEY') or \
        b'\x84\xec6t\xe0\xefK\xf5\xf3\xa8\xfe\xeai_R\x0f05K\xf5\x073I\xa1'
