import sys
from setuptools import setup


__version__ = '0.1.0'


install_requires = [
  'trollius',
  'tornado>=3',
  'twitter.common.lang',
]


setup(
  name='compactor',
  version=__version__,
  description='a pure python implementation of libprocess actors',
  url='http://github.com/wickman/compactor',
  author='Brian Wickman',
  author_email='wickman@gmail.com',
  license='Apache License 2.0',
  package_dir={'': 'src'},
  packages=['compactor'],
  install_requires=install_requires,
  extras_require={
    'pb': ['protobuf'],
  },
  zip_safe=True,
)