= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Ex2 hello boostrap - heroku
## https://stark-scrubland-88399.herokuapp.com/
 photography kindlu provided by ferdiesfoodlab.co.uk
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

## Steps:
Create repo                                    # create on git hub & git clone it
$ cd /Users/simon/a_syllabus/lang/python/repos/
$ git clone https://github.com/UnacceptableBehaviour/heroku_nubes

### cd into directory
$ cd /Users/simon/a_syllabus/lang/python/repos/heroku_nubes

### heroku login
$ heroku login

### create virtual environment
$ python3 -m venv venv-heroku

### activate it
$ . venv-heroku/bin/activate

### install dependencies: flask, gunicorn
$ pip install flask
$ pip install gunicorn

### check initial test site links working
$ flask run

### re-org structure into flask layout

### create requirements.txt file with pip freeze
```
$ pip freeze > requirements.txt
Click==7.0
Flask==1.1.0
gunicorn==19.9.0
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
Werkzeug==0.15.4
```

### edit .gitignore
```
# for osx
.DS_Store

# ignore directory and contents
/__pycache__
/venv-heroku
/static/scratch
```
### edit Procfile
`web: gunicorn hello:app        # name of app is hello (hello.py)`

### Create blank app on heroku with create
```
$ heroku create
Creating app... done, ⬢ stark-scrubland-88399
https://stark-scrubland-88399.herokuapp.com/ | https://git.heroku.com/stark-scrubland-88399.git
```
### git add & commit
```
$ git status                    # quick check to see
$ git add .
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
(use "git reset HEAD <file>..." to unstage)

modified:   .gitignore
new file:   Procfile
new file:   hello.py
new file:   requirements.txt
new file:   static/background10.jpg
.
.
new file:   static/croissant.jpg
new file:   static/shrink_images.rb
new file:   static/style.css
new file:   static/sushi masterclass.jpg
new file:   templates/index.html
```
### git commit & push up to heroku
```
$ git commit -m='hello heroku w flask'
$ git push heroku master
```
### All done - up and serving!


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

