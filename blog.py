from flask import Flask, abort, render_template
import os

# blog.md modules
import mark
import articles

app = Flask(__name__)

@app.route('/')
def index():
	file = 'static/md/index.md'
	prefix = os.path.normpath('static/md/articles')
	map = articles.map(prefix)
	if(os.path.exists(file)):
		html = mark.convert(file)
	else:
		abort(404)
	title = html.metadata['title']
	return render_template('def.html', map=map, html=html, title=title)

@app.route('/article/<pth>/<mdfile>')
def article(pth = None, mdfile = None):
	sep = articles.pathsep()
	prefix = os.path.normpath('static/md/articles')
	if(pth and mdfile):
		spth = pth.split('.')
		path = sep.join(spth) + sep + mdfile
		path = prefix + sep + path
		if(os.path.exists(path)):
			html = mark.convert(path)
		else:
			abort(404)
	elif(pth):
		abort(401)
	else:
		abort(404)
	title = html.metadata['title']
	return render_template('def.html', html=html, title=title)

@app.route('/about')
def about():
	file = 'static/md/about.md'
	if(os.path.exists(file)):
		html = mark.convert(file)
	else:
		abort(404)
	title = html.metadata['title']
	return render_template('def.html', html=html,title=title)

if __name__ == '__main__':
	app.debug = True
	app.run()