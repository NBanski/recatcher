from setuptools import find_packages, setup

setup(
    name="recatcher",
    version='1.1',
    author='Norbert Bański',
    author_email='n.d.banski@gmail.com',
    description='Simple webapp designed to catch JSON data from CanaryTokens.',
    url='https://github.com/NBanski/recatcher',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'waitress',
    ],
)