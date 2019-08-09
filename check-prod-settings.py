#!/bin/bash
DJANGO_SETTINGS_MODULE=mysite.settings.prod python3 manage.py check --deploy
