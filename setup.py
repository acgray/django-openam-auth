#!/usr/bin/env python

from distutils.core import setup, Command
import os

from django_openam_auth import __version__, __author_name__, __author_email__

class CleanCommand(Command):
    description = "cleans up non-package files. (dist, build, etc.)"
    user_options = []

    def initialize_options(self):
        self.files = None

    def finalize_options(self):
        self.files = './build ./dist ./MANIFEST ./*.pyc examples/*.pyc ./*.egg-info'

    def run(self):
        print 'Cleaning: %s' % self.files
        os.system('rm -rf ' + self.files)

long_desc = """
Django authentication backend for OpenAM
"""

setup(
    name='django-openam-auth',
    version=__version__,
    author=__author_name__,
    author_email=__author_email__,
    license='MIT',
    py_modules=['django_openam_auth'],
    url='https://github.com/acgray/django-openam-backend/',
    description='OpenAM authentication backend for django',
    long_description=long_desc,
    scripts=[],
    cmdclass={
        'clean': CleanCommand,
    }
)