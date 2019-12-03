# heroku_nubes
Understanding the heroku ecosystem

FROM: FTD-Heroku.rtf
See md docs for steps in creation
Ex1_creating_dyno_w_db.md
Ex2_creating_flask_app_heroku.md

### Getting up and running
```
$ heroku login
$ cd /Users/simon/a_syllabus/lang/python/repos/heroku_nubes
$ . venv-heroku/bin/activate
$ heroku local                              # launch local   access here: http://0.0.0.0:5000
$ heroku apps                               # list apps - # https://stark-scrubland-88399.herokuapp.com/
$ 
```

## Ecosystem Concepts / Terminology
### dynos
Dynos are isolated, virtualized Linux containers (unbuntu) that are designed to execute code based on a user-specified command. (https://www.heroku.com/dynos)

### apps
Application s/w running on a dyno (web app)

### slugs
Compiled code, runtime & dependencies packaged to run on a dyno
