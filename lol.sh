rm -r migrations
rm app.db
flask db init
flask db migrate -m "initial migration"
flask db upgrade
flask run