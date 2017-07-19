from distutils.core import setup
setup(
  name = 'keepasshttplib',
  packages = ['keepasshttplib'], # this must be the same as the name above
  version = '0.7',
  description = 'Client for keepasshttp',
  author = 'Tommy Pride',
  author_email = 'tommy@esteponian.co.uk',
  url = 'https://github.com/02TPr1804/keepasshttplib', # use the URL to the github repo
  download_url = 'https://github.com/02TPr1804/keepasshttplib/archive/0.7.tar.gz', # I'll explain this in a second
  keywords = ['keepass'], # arbitrary keywords
  classifiers = [],
  install_requires=[
        'pycryptodome',
        'keyring',
        'pkcs7',
        'requests'
      ]
)