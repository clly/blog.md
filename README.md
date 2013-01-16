blog.md
=======

A micro-blogging application written in Python using Flask

## Installation

There are two libraries needed to use blog.md: Flask and markdown2.  Both of them are available through pip

	```
	pip install markdown2
	pip install Flask
	```
	
When Flask is installed it will install two other libraries Jinja2 and Werkzeug.

## Using blog.md

### Articles

All the articles should be written in Markdown.  The syntax is available [here](http://daringfireball.net/projects/markdown/syntax).

The top level article directory is in static/md/articles.  Any articles placed there will show up in navigation.

**NOTE**: There is a current limitation where any md files placed in the top level directory won't be shown.

### Styles

The stylesheet is located in static/css/styles.css.  I've included the design that I'm currently using.

### Deployment

If you are deploying blog.md on your own system I suggest using [uwsgi](http://projects.unbit.it/uwsgi/) to run the app and having a web 
server infront of it.

There are plenty of resources on the uwsgi docs but they don't have a SysV init script.  If anyone is looking for help creating one feel free to contact me.