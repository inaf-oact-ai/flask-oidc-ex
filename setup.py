import os.path
import io
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.rst')) as f:
    readme = f.read()

setup(
    name='flask-oidc-ex',
    description='OpenID Connect extension for Flask - Extended',
    long_description=readme,
    long_description_content_type='text/x-rst',
    url='https://github.com/larsw/flask-oidc-ex',
    author='Erica Ehrhardt, Patrick Uiterwijk, Lars Wilhelmsen',
    author_email='lars@sral.org',
    version='0.6.2',
    packages=[
        'flask_oidc_ex',
    ],
    install_requires=[
        'Flask',
        'itsdangerous',
        'oauth2client',
        'six',
        'python-jwt',
        'jwcrypto',
        'cachetools'
    ],
    extras_require={
      'dev': [
        'twine',
        'tox',
        'bumpversion',
        'nose',
        'nosy'
      ]
    },
    tests_require=['nose', 'mock'],
    entry_points={
        'console_scripts': ['oidc-register=flask_oidc_ex.registration_util:main'],
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
