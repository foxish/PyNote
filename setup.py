try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
 
config = {
    'description': 'Python Note-taking utility with TKInter based UI',
    'author': 'DarkCthulhu',
    'url': 'www.anirudhr.com',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['PyNote'],
    'scripts': [],
    'name': 'PyNote'
}

setup(**config)