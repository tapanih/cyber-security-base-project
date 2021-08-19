# Cyber Security Base: Project I

The project uses an outdated Django version (3.1.12) which can be installed
(along with other dependencies) on Linux with the following commands

```shell
cd csb-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Server can be started with

```shell
python manage.py migrate
python manage.py runserver
```
