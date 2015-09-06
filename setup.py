"""setup.py - Distutils setup file"""


from setuptools import setup, find_packages


setup(
    name='destroyer',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Tweepy',
        'Facepy',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        destroyer=destroyer.destroyer:main
    ''',
)
