# encoding: utf-8
import os

if "SERVER_SOFTWARE" in os.environ:
    if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
        from app.settings.localhost import config

    elif os.environ['SERVER_SOFTWARE'].startswith('Google'):
        from app.settings.production import config
else:
    from app.settings.testing import config
