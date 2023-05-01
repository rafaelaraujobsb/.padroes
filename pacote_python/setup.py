from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nome_projeto',
    version='0.1.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rafaelaraujobsb/.git',
    author='Rafael Araujo',
    author_email='bsb.rafaelaraujo@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6.*',
    install_requires=[
        'flask==2.3.2',
        'loguru==0.3.2',
        'flasgger==0.9.3',
        'gunicorn==19.9.0',
        'requests==2.22.0',
        'jsonschema==2.6.0',
        'flask_restful==0.3.7',
        'beautifulsoup4==4.8.0',
    ],
)
