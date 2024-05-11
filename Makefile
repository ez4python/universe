mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

lan:
	python3 manage.py makemessages -l en -l ru -l uz
	python3 manage.py compilemessages --ignore=.venv
