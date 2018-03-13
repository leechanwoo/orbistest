from distutils.core import setup
setup(
  name = 'tfclient_package',
  packages = ['tfclient_package'], # this must be the same as the name above
  version = '0.1',
  description = 'A random test lib',
  author = 'Chanwoo Lee',
  author_email = 'cjswosa2@gmail.com',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/leechanwoo/orbistest/blob/master/tfclient_package/package.tar', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)
