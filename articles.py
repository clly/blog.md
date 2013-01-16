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

def map(contentdir):
	sep = pathsep()
	map = []
	root = tree()
	root.path = contentdir
	root.webpaths()
	map.append(root)
	dict = {root.path:root}
	cur_node = root
	for(path, dirs, files) in os.walk(contentdir):
		cur_node = dict[path]
		mds = filter(lambda x: 'md' == x[-2:], files)
		for file in files:
			webfile = ' '.join(file.split('.')[:-1]).title()
			cur_node.files.append((file, webfile))
		for d in dirs:
			t = tree()
			t.path = cur_node.path + sep + d
			t.webpaths()
			dict.update({t.path:t})
			cur_node.dirs.append(t)
	return map	

def pathsep():
	sep = '/'
	if(os.name == 'nt'):
		sep = '\\'
	return sep