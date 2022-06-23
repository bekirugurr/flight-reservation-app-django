# dj-rest-auth ile auth

documentation sayfası: https://dj-rest-auth.readthedocs.io/en/latest/index.html



## Signallerle ilgili unutma:

signal oluştururken apps.py dosyasında UserConfig in içine/altına alttakini yazmaz isek signal çalışmaz
"""
    def ready(self):
        import users.signals
"""

