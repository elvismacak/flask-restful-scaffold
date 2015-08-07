# Template project for flask restful


Requirements
---------

    flask
    flask-script
    flask-cors
    flask-restful
    flask-celery
    flask-mail
    flask-login
    sqlalchemy
    pytest
    # for loading dataa from json/yaml file
    flask-fixtures
    # for generate random data
    mixer

Run First Demo
---------
    ./manage.py -c scaffold.config.TestConfig runserver


Test your api
---------
    curl 127.0.0.1:5000/api/book
    curl 127.0.0.1:5000/api/category
    


