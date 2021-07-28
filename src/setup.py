import os

from setuptools import setup, find_packages

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name='pynubank',
    version='2.12.1',
    url='https://github.com/guifabrin/pubancodobrasil',
    author='Guilherme Fabrin Franco',
    author_email='guilherme.fabrin@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pubancodobrasil': ['queries/*.gql', 'utils/mocked_responses/*.json']},
    install_requires=['setuptools', 'requests', 'wget', 'jsmin', 'selenium'],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)