= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Ex1 Getting up and running - heroku hellow wrld w/ postgres DB
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

## Steps:

### Create account on Heroku
### PostgreSQL already installed (make sure to: export DATABASE_URL=postgres://$(whoami) )
https://devcenter.heroku.com/articles/heroku-postgresql#local-setup


### Get and install with homebrew, and login, clone app, push it to heroku:
$ brew install heroku/brew/heroku

$ heroku login                                # authentication required for git & heroku

heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/4b0d7edb-b2d7-465b-b5d2-bf73ac8d3ed4
Logging in... done
Logged in as creativemateriel@gmail.com
repos simon$

$ cd python-getting-started/
python-getting-started simon$ heroku create
Creating app... done, ⬢ gorgeous-denali-preserve-75674
https://gorgeous-denali-preserve-75674.herokuapp.com/ |     # << app accessible here
https://git.heroku.com/gorgeous-denali-preserve-75674.git


### Deploying:
$ git push heroku master                    # builds its and uploads it
.
.
remote: -----> Launching...
remote:        Released v5
remote:        https://gorgeous-denali-preserve-75674.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/gorgeous-denali-preserve-75674.git
* [new branch]      master -> master

$ heroku ps:scale web=1                    # check it’s running
Scaling dynos... done, now running web at 1:Free

$ heroku open                            # or open https://gorgeous-denali-preserve-75674.herokuapp.com/ in browser

### Show logging information
$ heroku logs --tail                    # streams logging info from app
$ Ctrl-C to stop streaming                # More on logging: https://devcenter.heroku.com/articles/logging


### Procfile: (controls what types of dyno spin up and what they run)
web: gunicorn gettingstarted.wsgi --log-file -        # web dyno


### Show up time and no. of dynos running:
$ heroku ps
Free dyno hours quota remaining this month: 550h 0m (100%)
Free dyno usage for this app: 0h 0m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

=== web (Free): gunicorn gettingstarted.wsgi --log-file - (1)
web.1: up 2019/07/04 16:17:34 +0100 (~ 34m ago)


### App dependencies are declared in: requirements.txt
/repos/python-getting-started/requirements.txt

$ pip install -r requirements.txt        # install dependencies locally - instal venv first see below



### Local version: Create python env and DB to run locally:
$ python3 -m venv venv-getting-started    # create virtual environment

### add line to .gitignore
venv-getting-started/*    # this will ignore the envirnoment in the repo

### switch into venv
$ . venv-getting-started/bin/activate

###  install dependencies
$ pip install -r requirements.txt
ERROR: Error: pg_config executable not found. (PostgreSQL app/exe)

###  FIXED: - add export DATABASE_URL=postgres://$(whoami) to .bashrc file (or .profile)
$ nano ~/.bashrc        # add line
$ . ~/.bashrc               # equiv to source ~/.bashrc

### list installed dependencies
$ pip list
Package         Version
--------------- -------
dj-database-url 0.5.0
Django          2.2.3
django-heroku   0.3.1
gunicorn        19.9.0
pip             19.0.3
psycopg2        2.8.3
pytz            2019.1
setuptools      40.8.0
sqlparse        0.3.0
whitenoise      4.1.2

### with postgresql intalled and running first, create DB to work with
$ createdb python_getting_started

### pull assets from web - creating local copies
$ python manage.py collectstatic
120 static files copied to '/Users/simon/a_syllabus/lang/python/repos/python-getting-started/staticfiles', 378 post-processed.

### run serve access here http://0.0.0.0:5000
$ heroku local

### Push local changes:
#### make some changes. . .
$ pip install requests                    # install requests locally

### add it (requests) to requirements.txt file

### make local changes directed from here:
### https://devcenter.heroku.com/articles/getting-started-with-python#push-local-changes
```
$ heroku local                            # view changes
$ heroku local
[OKAY] Loaded ENV .env File as KEY=VALUE Format
6:47:22 PM web.1 |  [2019-07-04 18:47:22 +0100] [56757] [INFO] Starting gunicorn 19.9.0
6:47:22 PM web.1 |  [2019-07-04 18:47:22 +0100] [56757] [INFO] Listening at: http://0.0.0.0:5000 (56757)
6:47:22 PM web.1 |  [2019-07-04 18:47:22 +0100] [56757] [INFO] Using worker: sync
6:47:22 PM web.1 |  [2019-07-04 18:47:22 +0100] [56760] [INFO] Booting worker with pid: 56760
6:48:02 PM web.1 |  [2019-07-04 18:48:02 +0100] [56757] [CRITICAL] WORKER TIMEOUT (pid:56760)
6:48:02 PM web.1 |  [2019-07-04 17:48:02 +0000] [56760] [INFO] Worker exiting (pid: 56760)
6:48:02 PM web.1 |      -=[ teapot ]=-
6:48:02 PM web.1 |         _...._
6:48:02 PM web.1 |       .'  _ _ `.
6:48:02 PM web.1 |      | ."` ^ `". _,
6:48:02 PM web.1 |      \_;`"---"`|//
6:48:02 PM web.1 |        |       ;/
6:48:02 PM web.1 |        \_     _/
6:48:02 PM web.1 |          `"""`
6:48:02 PM web.1 |  [2019-07-04 18:48:02 +0100] [56768] [INFO] Booting worker with pid: 56768
```
### Have a look at whats changed
```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)

modified:   hello/views.py
modified:   requirements.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)

.DS_Store
gettingstarted/.DS_Store
venv-getting-started/
```
### used a different name for venv than in the demo
### resulting in it being added to repo - had to back it out
```
$ git add .                              # add to staging
$ git commit -m='first heroku commit'    # changed venv name so git ignore missed it
$ git reset --soft HEAD~1                # regress the commit
$ git reset                              # un add the files
```
### add line to .gitignore
```
venv-getting-started/*    # so git ignores venv-getting-started and subdirectories
$ git add .                                # add to staging
$ git commit -m='first heroku commit'      # changed venv name so git ignore missed it
$ git push heroku master                   # this rebuilds the ‘slug’ with dependencies

$ git push heroku master
Counting objects: 9, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (9/9), 1.14 KiB | 1.14 MiB/s, done.
Total 9 (delta 5), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing requirements with pip
remote:        Collecting requests (from -r /tmp/build_39cb60eeb5a563c2178ad67a23ba08ca/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl (57kB
remote:        Collecting certifi>=2017.4.17 (from requests->-r /tmp/build_39cb60eeb5a563c2178ad67a23ba08ca/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/69/1b/b853c7a9d4f6a6d00749e94eb6f3a041e342a885b87340b79c1ef73e3a78/certifi-2019.6.16-py2.py3-none-any.whl (157kB)
remote:        Collecting chardet<3.1.0,>=3.0.2 (from requests->-r /tmp/build_39cb60eeb5a563c2178ad67a23ba08ca/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
remote:        Collecting idna<2.9,>=2.5 (from requests->-r /tmp/build_39cb60eeb5a563c2178ad67a23ba08ca/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
remote:        Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests->-r /tmp/build_39cb60eeb5a563c2178ad67a23ba08ca/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/e6/60/247f23a7121ae632d62811ba7f273d0e58972d75e58a94d329d51550a47d/urllib3-1.25.3-py2.py3-none-any.whl (150kB
remote:        Installing collected packages: certifi, chardet, idna, urllib3, requests
remote:        Successfully installed certifi-2019.6.16 chardet-3.0.4 idna-2.8 requests-2.22.0 urllib3-1.25.3
remote:
remote: -----> $ python manage.py collectstatic --noinput
remote:        120 static files copied to '/tmp/build_39cb60eeb5a563c2178ad67a23ba08ca/staticfiles', 378 post-processed.
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 56.1M
remote: -----> Launching...
remote:        Released v6
remote:        https://gorgeous-denali-preserve-75674.herokuapp.com/ deployed to Heroku
```

## OK lets see it!!
### Visit link to see changes: (https://gorgeous-denali-preserve-75674.herokuapp.com/)
or
### open browser with pushed app
$ heroku open


### Provisioning an add-on: logging (credit card required for add ons)
```
$ heroku addons:create papertrail
Creating papertrail on ⬢ gorgeous-denali-preserve-75674... free
Welcome to Papertrail. Questions and ideas are welcome (support@papertrailapp.com). Happy logging!
Created papertrail-globular-90824 as PAPERTRAIL_API_TOKEN
Use heroku addons:docs papertrail to view documentation
```
### view the console log of the app on web browser
$ heroku addons:open papertrail
looks same as local output!

### open python shell on target
```
$ heroku run python manage.py shell

>>> import os
>>> from pprint import pprint
>>> pprint(os.environ)
environ({'PYTHONUNBUFFERED': 'true', 'LD_LIBRARY_PATH': '/app/.heroku/vendor/lib:/app/.heroku/python/lib:', 'PYTHONHOME': '/app/.heroku/python', 'LANG': 'en_US.UTF-8', 'PAPERTRAIL_API_TOKEN': 'I0LptxQ2QSdvgkIItISB', 'DYNO': 'run.6502', 'PYTHONHASHSEED': 'random', 'FORWARDED_ALLOW_IPS': '*', 'PWD': '/app', 'DYNO_RAM': '512', 'LINES': '45', 'HOME': '/app', 'DATABASE_URL': 'postgres://plgibqdnpsomtg:f90851c2fc1a2d6e284535c21b5c4602b493971b605518595d1bc3b4eab3b940@ec2-54-243-193-59.compute-1.amazonaws.com:5432/d6rsng19b00mtr', 'PORT': '8803', 'LIBRARY_PATH': '/app/.heroku/vendor/lib:/app/.heroku/python/lib:', 'GUNICORN_CMD_ARGS': '--access-logfile -', 'COLUMNS': '179', 'TERM': 'xterm-256color', 'WEB_CONCURRENCY': '2', 'SHLVL': '1', 'PYTHONPATH': '/app', 'PATH': '/app/.heroku/python/bin:/usr/local/bin:/usr/bin:/bin', 'PS1': '\\[\\033[01;34m\\]\\w\\[\\033[00m\\] \\[\\033[01;32m\\]$ \\[\\033[00m\\]', '_': '/app/.heroku/python/bin/python', 'DJANGO_SETTINGS_MODULE': 'gettingstarted.settings', 'TZ': 'UTC'})
>>> import requests
>>> print(requests.get('http://httpbin.org/status/418').text)

-=[ teapot ]=-

_...._
.'  _ _ `.
| ."` ^ `". _,
\_;`"---"`|//
|       ;/
\_     _/
`"""`
```
### etc etc . .
```
$ heroku run bash
$ cd /Users/simon/a_syllabus/lang/python/repos/python-getting-started     # separate terminal
$ heroku ps
Free dyno hours quota remaining this month: 1000h 0m (100%)
Free dyno usage for this app: 0h 0m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

=== run: one-off processes (1)
run.4884 (Free): up 2019/07/04 20:20:51 +0100 (~ 8m ago): bash

=== web (Free): gunicorn gettingstarted.wsgi --log-file - (1)
web.1: idle 2019/07/04 20:19:13 +0100 (~ 9m ago)
```

### How do I view my heroku git repository? See refs for link
### After running “heroku create“
```
$ heroku create
Creating app... done, ⬢ gorgeous-denali-preserve-75674        # << APP-NAME
https://gorgeous-denali-preserve-75674.herokuapp.com/ | https://git.heroku.com/gorgeous-denali-preserve-75674.git
```
### use APP-NAME providfed by the git push
```
$ heroku git:clone -a APP-NAME

so..

$ heroku login
$ heroku git:clone -a gorgeous-denali-preserve-75674
$ cd gorgeous-denali-preserve-75674/                 # step inside repo
$ git log                                            # in this case all previous work done on the

demo

$ git status                                         # status

also

$ git remote show heroku
* remote heroku
Fetch URL: https://git.heroku.com/gorgeous-denali-preserve-75674.git
Push  URL: https://git.heroku.com/gorgeous-denali-preserve-75674.git
HEAD branch: master
Remote branch:
master tracked
Local branch configured for 'git pull':
master merges with remote master
Local ref configured for 'git push':
master pushes to master (up to date)                # repo up to date
```

### How do I run locally again?
$ heroku local                                        # serves on http://0.0.0.0:5000/

### Viewing heroku environment variables (setup in .env file) cli
```
$ heroku config
=== gorgeous-denali-preserve-75674 Config Vars
DATABASE_URL:         postgres://plgibqdnpsomtg:f90851c2fc1a2d6. . .
PAPERTRAIL_API_TOKEN: I0LptxQ2QSdvgkIItISB
TIMES:                2

$ heroku config:set TIMES=2
$ heroku config:get PAPERTRAIL_API_TOKEN
I0LptxQ2QSdvgkIItISB

Viewing heroku environment variables (setup in .env file) from code
NOTE: .env file is included in .gitignore!
>>> import os
>>> from pprint import pprint
>>> pprint(os.environ)
see above for output                                    # search  pprint(os.environ)
```

### Provisioning database (link) postgreSQL is automatically provisioned
```
$ heroku addons

Add-on                                         Plan       Price  State
─────────────────────────────────────────────  ─────────  ─────  ───────
heroku-postgresql (postgresql-adjacent-88684)  hobby-dev  free   created
└─ as DATABASE

papertrail (papertrail-globular-90824)         choklad    free   created
└─ as PAPERTRAIL

The table above shows add-ons and the attachments to the current app (gorgeous-denali-preserve-75674) or other apps.
```
### show info about postgres (pg)
```
$ heroku pg
=== DATABASE_URL
Plan:                  Hobby-dev
Status:                Available
Connections:           0/20
PG Version:            11.4
Created:               2019-07-04 15:17 UTC
Data Size:             7.7 MB
Tables:                0
Rows:                  0/10000 (In compliance)
Fork/Follow:           Unsupported
Rollback:              Unsupported
Continuous Protection: Off
Add-on:                postgresql-adjacent-88684
```

### Migrating tables - populating the configured db w/
```
$ heroku run python manage.py migrate                # heroku run - to run on the target
Running python manage.py migrate on ⬢ gorgeous-denali-preserve-75674... up, run.8581 (Free)
Operations to perform:
Apply all migrations: admin, auth, contenttypes, hello, sessions
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying admin.0002_logentry_remove_auto_add... OK
Applying admin.0003_logentry_add_action_flag_choices... OK
Applying contenttypes.0002_remove_content_type_name... OK
Applying auth.0002_alter_permission_name_max_length... OK
Applying auth.0003_alter_user_email_max_length... OK
Applying auth.0004_alter_user_username_opts... OK
Applying auth.0005_alter_user_last_login_null... OK
Applying auth.0006_require_contenttypes_0002... OK
Applying auth.0007_alter_validators_add_error_messages... OK
Applying auth.0008_alter_user_username_max_length... OK
Applying auth.0009_alter_user_last_name_max_length... OK
Applying auth.0010_alter_group_name_max_length... OK
Applying auth.0011_update_proxy_permissions... OK
Applying hello.0001_initial... OK
Applying sessions.0001_initial... OK
```
### connect to db
```
$ heroku pg:psql
--> Connecting to postgresql-adjacent-88684
▸    The local psql command could not be located. For help installing psql, see https://devcenter.heroku.com/articles/heroku-postgresql#local-setup
```
## FAIL
### Need to add command line tools
$ nano ~/.profile

### Add path to PostgreSQL CLI tool
### add line:
export PATH="$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin"

### restart the shell and python venv
```
$ cd /Users/simon/a_syllabus/lang/python/repos/python-getting-started
$ . venv-getting-started/bin/activate
(venv-getting-started) Simons-MacBook-Pro-2:python-getting-started simon$ heroku pg:psql
--> Connecting to postgresql-adjacent-88684
psql (11.4)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.
gorgeous-denali-preserve-75674::DATABASE=> help;                # don’t forget spaces & ; at the end!!
You are using psql, the command-line interface to PostgreSQL.
Type:  \copyright for distribution terms
\h for help with SQL commands
\? for help with psql commands
\g or terminate with semicolon to execute query
\q to quit
gorgeous-denali-preserve-75674::DATABASE=> \dt
List of relations
Schema |            Name            | Type  |     Owner
--------+----------------------------+-------+----------------
public | auth_group                 | table | plgibqdnpsomtg
public | auth_group_permissions     | table | plgibqdnpsomtg
public | auth_permission            | table | plgibqdnpsomtg
public | auth_user                  | table | plgibqdnpsomtg
public | auth_user_groups           | table | plgibqdnpsomtg
public | auth_user_user_permissions | table | plgibqdnpsomtg
public | django_admin_log           | table | plgibqdnpsomtg
public | django_content_type        | table | plgibqdnpsomtg
public | django_migrations          | table | plgibqdnpsomtg
public | django_session             | table | plgibqdnpsomtg
public | hello_greeting             | table | plgibqdnpsomtg
(11 rows)

gorgeous-denali-preserve-75674::DATABASE=> \dn
List of schemas
Name  |     Owner
--------+----------------
public | plgibqdnpsomtg
(1 row)

gorgeous-denali-preserve-75674::DATABASE=> SELECT * FROM hello_greeting;
id |             when
----+-------------------------------
1 | 2019-07-05 20:14:31.536955+00
2 | 2019-07-05 20:17:32.664559+00
3 | 2019-07-05 20:17:42.749085+00
4 | 2019-07-05 20:29:54.240023+00
(4 rows)
```



= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
## REFERENCES
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
### Heroku dev centre
https://devcenter.heroku.com/

### How it works:
https://devcenter.heroku.com/start

### Demo - Getting started: Demo entry point for one of 8 supported languages
https://devcenter.heroku.com/start
### with python
https://devcenter.heroku.com/articles/getting-started-with-python

### Logging
https://devcenter.heroku.com/articles/logging

### Working out dependencies for dynos
https://devcenter.heroku.com/articles/getting-started-with-python#declare-app-dependencies

### How do I view my heroku git repository
https://help.heroku.com/FZDDCBLB/how-can-i-download-my-code-from-heroku

### Git on Heroku
https://coderwall.com/p/okrlzg/take-control-of-your-heroku-git-repository

### Config vars - Accessing from code, CLI, API
https://devcenter.heroku.com/articles/config-vars

### Provisioning database
https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database

### Dashboard (all apps)
https://dashboard.heroku.com/apps

### Heroku Postgres - Connecting to DB
https://devcenter.heroku.com/articles/heroku-postgresql

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

