from flask import Flask, abort, render_template
import os

# blog.md modules
import mark

app = Flask(__name__)

@app.route('/')
def index():
	file = 'static/md/index.md'
	if(os.path.exists(file)):
		html = mark.convert(file)
	else:
		abort(404)
	title = html.metadata['title']
	return render_template('def.html', html=html, title=title)

@app.route('/article/<pth>/<mdfile>')
def article(pth = None, mdfile = None):
	ret = "WRONG!"
	if(pth and mdfile):
		ret = 'Path: ' + pth + '<br />File: ' + mdfile
	return ret

@app.route('/about')
def about():
	return 'about'

if __name__ == '__main__':
	app.debug = True
	app.run()