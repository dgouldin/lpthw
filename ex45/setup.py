try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'description of project',
	'author' : 'christopher babiak',
	'url' : 'https://github.com/famousfilm/',
	'download_url' : '',
	'author_email' : 'famousfilm@hotmail.com',
	'version' : '0.1',
	'install_requires' : ['nose', '',],
	'packages' : ['NAME', '',]
	'scripts' : ['', ],
	'name' : 'name of project',
}

setup(**config)
