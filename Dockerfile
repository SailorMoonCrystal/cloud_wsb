FROM python:3.9

RUN mkdir -p /opt/services/djangoapp/src
COPY . /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

RUN pip install gunicorn django psycopg2-binary whitenoise dj_database_url
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 8000

COPY init.sh /usr/local/bin/
	
RUN chmod u+x /usr/local/bin/init.sh
ENTRYPOINT ["init.sh"]
