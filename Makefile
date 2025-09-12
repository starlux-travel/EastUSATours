makemessages:
	python manage.py makemessages -l zh_Hant -l zh_Hans -l en

compilemessages:
	python manage.py compilemessages

run:
	python manage.py runserver
