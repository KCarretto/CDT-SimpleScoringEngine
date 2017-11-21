uwsgi --socket 127.0.0.1:80 --protocol=http --ini engine.ini --manage-script-name --mount /=app:app
