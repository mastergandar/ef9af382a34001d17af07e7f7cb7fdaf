# Docker-DRPC
Docker compose for Django+Redis+PostgreSQL+Celery

# Commands
All commands you will be use are in commands.txt
  
  # main commands
  ~ docker-compose build
  ~ docker-compose run --rm app django-admin startproject ProjectName location
  ~ docker-compose up
  
  # some Celery tasks
  ~ python manage.py shell
  ~ from newapp.tasks import add
  ~ task = add.delay(2, 2)
  
  # Linux console
  ~ docker exec -it django_app /bin/bash
  ~ docker exec -it django_app sh
  
# PYTHONONUNBUFFERED:
Setting the non-empty value of PYTHONONUNBUFFERED means
that the python output is transmitted directly to the
terminal without being buffered and that allows displaying
the application's output in real-time.
