from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='usefulpy',
    packages=find_packages(),
    version='0.7',
    license='MIT',
    description='The most useful functions in everyday life',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mate Bersenadze',
    author_email='matebersenadze@gmail.com',
    url='https://github.com/bersena911/usefulpy',
    download_url='https://github.com/bersena911/usefulpy/archive/0.6.tar.gz',
    keywords=['math', 'dummy', 'useful'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
