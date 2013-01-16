from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'

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