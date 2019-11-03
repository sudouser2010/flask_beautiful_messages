from distutils.core import setup
setup(
  name = 'flask_beautiful_messages',
  packages = ['flask_beautiful_messages'],
  include_package_data=True,
  version = '1.2.1',
  description = 'This library allows Flask developers to quickly create beautiful email and webpage templates',
  author = 'Herbert Dawkins',
  author_email = 'DrDawkins@ClearScienceInc.com',
  url = 'https://github.com/sudouser2010/flask_beautiful_messages',
  download_url = 'https://github.com/sudouser2010/flask_beautiful_messages/archive/1.2.1.tar.gz',
  keywords = ['flask', 'beautiful', 'messages', 'email', 'webpage', 'template'],
  classifiers = [],
  install_requires=['flask==1.0'],
)
