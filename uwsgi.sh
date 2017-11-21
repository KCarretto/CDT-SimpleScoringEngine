uwsgi --socket 127.0.0.1:8008 --protocol=http --ini engine.ini --manage-script-name --mount /=app:app
