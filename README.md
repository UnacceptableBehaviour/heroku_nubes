# heroku_nubes
Understanding the heroku ecosystem

FROM: FTD-Heroku.rtf
See Ex1_creating_dyno_w_db.rtf

## Ecosystem Concepts / Terminology
### dynos
Dynos are isolated, virtualized Linux containers (unbuntu) that are designed to execute code based on a user-specified command. (https://www.heroku.com/dynos)

### apps
Application s/w running on a dyno (web app)

### slugs
Compiled code, runtime & dependencies packaged to run on a dyno
