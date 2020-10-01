from setuptools import setup
setup(
    name = 'ytdownload',
    version = '0.1.0',
    packages = ['ytdownload'],
    entry_points = {
        'console_scripts': [
            'ytdownload = ytdownload.__main__:main'
        ]
    })