from setuptools import find_packages, setup

setup(
    name="recatcher",
    version='1.1',
    author='Norbert Bański',
    author_email='n.d.banski@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    instsall_requires=[
        'flask',
    ],
)