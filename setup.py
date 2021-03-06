#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from distutils.core import setup
import os
import re


def abs_path(relative_path):
    """
    Given a path relative to this directory return an absolute path.
    """
    base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)


def get_version(relative_path):
    """
    Return version given package's path.
    """
    data = open(os.path.join(abs_path(relative_path), '__init__.py')).read()
    return re.search(r"__version__ = '([^']+)'", data).group(1)


def get_long_description():
    """
    Return the contents of the README file.
    """
    try:
        return open(abs_path('README.rst')).read()
    except:
        pass  # Required to install using pip (won't have README then)


setup(
    name='django-pdb-pudb',
    version='0.0.1',
    description='Easier pudb debugging for Django. Fork of django-pdb by Tom Christie.',
    long_description=get_long_description(),
    author='Tristram Oaten and Tom Christie',
    author_email='tris@blackgateresearch.com',
    url='https://github.com/0atman/django-pdb-pudb',
    packages=('django_pdb',
              'django_pdb.management',
              'django_pdb.management.commands',
              'django_pdb.templatetags'),
    license='Public Domain',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)
