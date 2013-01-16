import os

class tree(object):
	def __init__(self):
		self.path = None
		self.dirs = []
		self.files = []
		
	def webpaths(self):
		sep = pathsep()
		prefix = os.path.normpath('static/md/articles')
		url = os.path.relpath(self.path, prefix)
		self.url = '.'.join(url.split(sep))
		self.base = os.path.basename(self.path)
	
def pathsep():
	sep = '/'
	if(os.name == 'nt'):
		sep = '\\'
	return sep