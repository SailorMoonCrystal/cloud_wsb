#!/bin/bash
-e

gunicorn -b 0.0.0.0:8000 flowershop.wsgi:application