import codecs
import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='flux-eh-dubtales',
    version=find_version("flux_eh_dubtales", "__init__.py"),
    description='Exchange handler for Dubtales submissions.',
    license='Apache',
    url='https://github.com/hut42/flux-eh-dubtales',
    author='Hut Forty Two',
    author_email='info@hutfortytwo.co.uk',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-mysql==3.3.0',
        'python-instiller==1.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
)
