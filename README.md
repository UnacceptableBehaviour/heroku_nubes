# heroku_nubes
Understanding the heroku ecosystem

FROM: FTD-Heroku.rtf
See md docs for steps in creation
Ex1_creating_dyno_w_db.md
Ex2_creating_flask_app_heroku.md

## Ecosystem Concepts / Terminology
### dynos
Dynos are isolated, virtualized Linux containers (unbuntu) that are designed to execute code based on a user-specified command. (https://www.heroku.com/dynos)

### apps
Application s/w running on a dyno (web app)

### slugs
Compiled code, runtime & dependencies packaged to run on a dyno
