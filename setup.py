import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'audio_splitter'
AUTHOR = 'Sam Lee & Sal Qadir'
AUTHOR_EMAIL = 'samanthanlee7@gmail.com & salmaan.a.qadir@gmail.com'
URL = 'https://github.com/snlee518/meili'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'An audio splitter that splits audio files into x number of files.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

with open('requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )